"""Class 54: custom BaseLoader for one or many text files.

Run: python practice/class54_custom_text_loader.py
"""

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator

from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document


class SimpleTextLoader(BaseLoader):
    def __init__(self, path: Path):
        self.path = Path(path)

    def lazy_load(self) -> Iterator[Document]:
        yield Document(
            page_content=self.path.read_text(encoding="utf-8"),
            metadata={"source": str(self.path)},
        )


class FolderTextLoader(BaseLoader):
    def __init__(self, folder: Path):
        self.folder = Path(folder)

    def lazy_load(self) -> Iterator[Document]:
        for path in sorted(self.folder.glob("*.txt")):
            yield from SimpleTextLoader(path).lazy_load()


if __name__ == "__main__":
    with TemporaryDirectory(dir=Path(__file__).parent) as temp:
        folder = Path(temp)
        (folder / "a.txt").write_text("First document", encoding="utf-8")
        (folder / "b.txt").write_text("Second document", encoding="utf-8")
        one = SimpleTextLoader(folder / "a.txt").load()
        many = FolderTextLoader(folder).load()
        assert len(one) == 1 and len(many) == 2
        print("One:", one[0])
        print("Many:", many)
