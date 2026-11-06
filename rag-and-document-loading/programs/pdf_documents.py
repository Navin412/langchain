"""Class 55: convert each readable PDF page to a Document."""

import argparse
from pathlib import Path

from langchain_core.documents import Document
from pypdf import PdfReader


def load_pdf(path: Path) -> list[Document]:
    reader = PdfReader(str(path))
    return [
        Document(
            page_content=page.extract_text() or "",
            metadata={"source": str(path), "source_type": "pdf", "page": index},
        )
        for index, page in enumerate(reader.pages)
    ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()
    documents = load_pdf(args.pdf)
    print(f"Pages: {len(documents)}")
    for document in documents[:3]:
        print(document.metadata, repr(document.page_content[:120]))
    if any(not document.page_content.strip() for document in documents):
        print("At least one page has no extracted text; a scan may need OCR.")
