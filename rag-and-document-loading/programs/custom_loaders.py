"""Class 54/56: small custom text and CSV loaders, with no model call."""

import csv
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator

from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document


class TextFileLoader(BaseLoader):
    def __init__(self, path: Path):
        self.path = Path(path)

    def lazy_load(self) -> Iterator[Document]:
        yield Document(
            page_content=self.path.read_text(encoding="utf-8"),
            metadata={"source": str(self.path), "source_type": "txt"},
        )


class CSVRowsLoader(BaseLoader):
    def __init__(self, path: Path):
        self.path = Path(path)

    def lazy_load(self) -> Iterator[Document]:
        with self.path.open(newline="", encoding="utf-8") as stream:
            for row_number, row in enumerate(csv.DictReader(stream), start=1):
                content = "\n".join(f"{key}: {value}" for key, value in row.items())
                yield Document(
                    page_content=content,
                    metadata={
                        "source": str(self.path),
                        "source_type": "csv",
                        "row": row_number,
                    },
                )


if __name__ == "__main__":
    with TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        text_path = root / "rules.txt"
        text_path.write_text("Library opens at 8 AM.\n", encoding="utf-8")
        csv_path = root / "students.csv"
        csv_path.write_text("name,course\nRavi,Python\nAnu,AI\n", encoding="utf-8")
        text_docs = TextFileLoader(text_path).load()
        csv_docs = CSVRowsLoader(csv_path).load()
        assert len(text_docs) == 1 and len(csv_docs) == 2
        print(text_docs[0])
        print(csv_docs[0])
