"""Class 49: TextLoader, metadata, multiple files, missing files and lazy_load.

Run: python practice/class49_text_loader.py
"""

from pathlib import Path
from tempfile import TemporaryDirectory

from langchain_community.document_loaders import TextLoader


def program_1_first_loader(path: Path):
    documents = TextLoader(str(path), encoding="utf-8").load()
    print("Content:", documents[0].page_content.strip())
    return documents


def program_2_return_type_and_metadata(path: Path):
    documents = TextLoader(str(path), encoding="utf-8").load()
    print("Return type:", type(documents).__name__)
    print("Document metadata:", documents[0].metadata)
    return documents


def program_3_multiple_files(folder: Path):
    return [
        document
        for path in sorted(folder.glob("*.txt"))
        for document in TextLoader(str(path), encoding="utf-8").load()
    ]


def program_4_missing_file(path: Path) -> str:
    try:
        TextLoader(str(path), encoding="utf-8").load()
    except RuntimeError as error:
        return str(error)
    raise AssertionError("Expected the missing file to fail")


def program_5_lazy_load(path: Path):
    return list(TextLoader(str(path), encoding="utf-8").lazy_load())


if __name__ == "__main__":
    with TemporaryDirectory(dir=Path(__file__).parent) as temp:
        folder = Path(temp)
        (folder / "rules.txt").write_text("Bring an ID card.\n", encoding="utf-8")
        (folder / "hours.txt").write_text("Classes start at 9 AM.\n", encoding="utf-8")
        assert len(program_1_first_loader(folder / "rules.txt")) == 1
        assert program_2_return_type_and_metadata(folder / "rules.txt")[0].metadata["source"]
        assert len(program_3_multiple_files(folder)) == 2
        assert "missing" in program_4_missing_file(folder / "missing.txt")
        assert len(program_5_lazy_load(folder / "rules.txt")) == 1
        print("All Class 49 exercises passed")
