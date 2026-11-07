"""Class 55: four PDF exercises using pypdf and LangChain core.

Run: python practice/class55_pdf_core.py path/to/a.pdf
"""

import argparse
from pathlib import Path
from typing import Iterator

from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document
from pypdf import PdfReader


def program_1_single_page(path: Path) -> Document:
    reader = PdfReader(str(path))
    return Document(
        page_content=reader.pages[0].extract_text() or "",
        metadata={"source": str(path), "page": 0},
    )


def program_2_multiple_pages(path: Path) -> list[Document]:
    reader = PdfReader(str(path))
    return [
        Document(
            page_content=page.extract_text() or "",
            metadata={"source": str(path), "page": index},
        )
        for index, page in enumerate(reader.pages)
    ]


def program_3_whole_pdf(path: Path) -> Document:
    pages = program_2_multiple_pages(path)
    return Document(
        page_content="\n\n".join(page.page_content for page in pages),
        metadata={"source": str(path), "total_pages": len(pages)},
    )


class CustomPDFLoader(BaseLoader):
    def __init__(self, path: Path):
        self.path = Path(path)

    def lazy_load(self) -> Iterator[Document]:
        yield from program_2_multiple_pages(self.path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()
    first = program_1_single_page(args.pdf)
    pages = program_2_multiple_pages(args.pdf)
    whole = program_3_whole_pdf(args.pdf)
    custom = CustomPDFLoader(args.pdf).load()
    assert len(pages) == len(custom) == whole.metadata["total_pages"]
    print("First page:", first.metadata, repr(first.page_content[:100]))
    print("Page count:", len(pages), "Whole document chars:", len(whole.page_content))
