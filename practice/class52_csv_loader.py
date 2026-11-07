"""Class 52: CSVLoader basic, file creation, content/metadata and CSV options.

Run: python practice/class52_csv_loader.py
"""

from pathlib import Path
from tempfile import TemporaryDirectory

from langchain_community.document_loaders import CSVLoader


def program_1_basic(path: Path):
    return CSVLoader(str(path), encoding="utf-8").load()


def program_1a_create_actual_csv(folder: Path):
    path = folder / "students.csv"
    path.write_text(
        "student_id,name,course,fee\nS101,Ravi,Python,5000\nS102,Priya,Java,6000\n",
        encoding="utf-8",
    )
    return path, program_1_basic(path)


def program_2_content_and_metadata(path: Path):
    return CSVLoader(
        str(path),
        encoding="utf-8",
        content_columns=("name", "course"),
        metadata_columns=("student_id",),
    ).load()


def program_3_source_and_csv_args(folder: Path):
    path = folder / "semicolon.csv"
    path.write_text("url;name;course\nexample.org/ravi;Ravi;Python\n", encoding="utf-8")
    return CSVLoader(
        str(path),
        encoding="utf-8",
        source_column="url",
        csv_args={"delimiter": ";"},
    ).load()


if __name__ == "__main__":
    with TemporaryDirectory(dir=Path(__file__).parent) as temp:
        folder = Path(temp)
        path, basic = program_1a_create_actual_csv(folder)
        selected = program_2_content_and_metadata(path)
        custom = program_3_source_and_csv_args(folder)
        assert len(basic) == len(selected) == 2
        assert selected[0].metadata["student_id"] == "S101"
        assert custom[0].metadata["source"] == "example.org/ravi"
        print("Basic:", basic[0])
        print("Selected columns:", selected[0])
        print("Custom separator/source:", custom[0])
