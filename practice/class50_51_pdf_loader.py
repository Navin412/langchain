"""Classes 50–51: five PyPDFLoader exercises shared by both PDFs.

Run: python practice/class50_51_pdf_loader.py
Or:  python practice/class50_51_pdf_loader.py path/to/your.pdf
"""

import argparse
from pathlib import Path
from tempfile import TemporaryDirectory

from langchain_community.document_loaders import PyPDFLoader
from pypdf import PdfWriter


def program_1_first_pdf(path: Path):
    return PyPDFLoader(str(path)).load()


def program_2_multiple_pages(path: Path):
    documents = program_1_first_pdf(path)
    for document in documents:
        print("Page:", document.metadata.get("page"), "chars:", len(document.page_content))
    return documents


def program_3_pdf_metadata(path: Path):
    return [document.metadata for document in program_1_first_pdf(path)]


def program_4_page_versus_single(path: Path):
    page_documents = PyPDFLoader(str(path), mode="page").load()
    single_document = PyPDFLoader(str(path), mode="single").load()
    return page_documents, single_document


def program_5_lazy_and_empty_pages(path: Path):
    documents = list(PyPDFLoader(str(path), mode="page").lazy_load())
    empty_pages = [document.metadata.get("page") for document in documents if not document.page_content.strip()]
    return documents, empty_pages


def make_demo_pdf(path: Path) -> None:
    """Make two blank pages to practice metadata and empty-page detection offline."""
    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)
    writer.add_blank_page(width=612, height=792)
    with path.open("wb") as stream:
        writer.write(stream)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", nargs="?", type=Path)
    args = parser.parse_args()
    with TemporaryDirectory(dir=Path(__file__).parent) as temp:
        path = args.pdf or Path(temp) / "two_blank_pages.pdf"
        if args.pdf is None:
            make_demo_pdf(path)
        print("Loaded:", len(program_1_first_pdf(path)))
        program_2_multiple_pages(path)
        print("Metadata:", program_3_pdf_metadata(path))
        pages, whole = program_4_page_versus_single(path)
        print("Page mode:", len(pages), "Single mode:", len(whole))
        lazy, empty = program_5_lazy_and_empty_pages(path)
        print("Lazily loaded:", len(lazy), "Empty page numbers:", empty)
        assert len(whole) == 1 and len(pages) == len(lazy)
