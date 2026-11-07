"""Class 56: two CSV-to-Document programs from the ChatGPT study note.

Run: python practice/class56_csv_core.py
"""

import csv
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator

from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document


def program_1_csv_records(path: Path) -> list[Document]:
    documents = []
    with path.open("r", encoding="utf-8", newline="") as stream:
        for row_index, row in enumerate(csv.DictReader(stream)):
            documents.append(
                Document(
                    page_content="\n".join(f"{field}: {value}" for field, value in row.items()),
                    metadata={"source": str(path), "source_type": "csv", "row": row_index},
                )
            )
    return documents


class StudentCSVLoader(BaseLoader):
    """Program 2: choose CSV fields for text and fields for metadata."""

    def __init__(self, path: Path):
        self.path = Path(path)

    def lazy_load(self) -> Iterator[Document]:
        with self.path.open("r", encoding="utf-8", newline="") as stream:
            for row_index, row in enumerate(csv.DictReader(stream)):
                yield Document(
                    page_content=f"name: {row['name']}\nfee: {row['fee']}",
                    metadata={
                        "source": str(self.path),
                        "source_type": "csv",
                        "row": row_index,
                        "student_id": row["student_id"],
                        "course": row["course"],
                    },
                )


if __name__ == "__main__":
    with TemporaryDirectory(dir=Path(__file__).parent) as temp:
        path = Path(temp) / "students.csv"
        path.write_text(
            "student_id,name,course,fee\n"
            "S101,Ravi,Python,5000\n"
            "S102,Priya,Java,6000\n",
            encoding="utf-8",
        )
        all_fields = program_1_csv_records(path)
        selected = StudentCSVLoader(path).load()
        assert len(all_fields) == len(selected) == 2
        assert "student_id" in all_fields[0].page_content
        assert "student_id" not in selected[0].page_content
        assert selected[0].metadata["student_id"] == "S101"
        print("All fields:", all_fields[0])
        print("Selected fields:", selected[0])
