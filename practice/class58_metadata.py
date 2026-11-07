"""Class 58: metadata enrichment, numbering and a multi-format inspector.

Run: python practice/class58_metadata.py
"""

import csv
from pathlib import Path
from tempfile import TemporaryDirectory

from bs4 import BeautifulSoup
from langchain_core.documents import Document
from pypdf import PdfReader, PdfWriter


def program_1_enrich(document: Document, source_type: str, category: str) -> Document:
    return Document(
        page_content=document.page_content,
        metadata={**document.metadata, "source_type": source_type, "category": category},
    )


def program_2_human_number(document: Document) -> int | None:
    """LangChain loaders commonly use zero-based page or row metadata."""
    position = document.metadata.get("page", document.metadata.get("row"))
    return None if position is None else int(position) + 1


def program_3_standardize(document: Document) -> Document:
    metadata = dict(document.metadata)
    metadata.setdefault("source", "unknown")
    metadata.setdefault("source_type", "unknown")
    if "page" in metadata:
        metadata["display_page"] = int(metadata["page"]) + 1
    if "row" in metadata:
        metadata["display_row"] = int(metadata["row"]) + 1
    return Document(page_content=document.page_content, metadata=metadata)


def program_4_inspect(documents: list[Document]) -> list[dict]:
    return [
        {
            "source": document.metadata.get("source", "unknown"),
            "type": document.metadata.get("source_type", "unknown"),
            "characters": len(document.page_content),
            "has_text": bool(document.page_content.strip()),
            "human_position": program_2_human_number(document),
        }
        for document in documents
    ]


def program_4_multiformat_demo() -> tuple[list[Document], list[dict]]:
    """Create TXT/CSV/HTML samples and inspect two pages from a supplied PDF."""
    source_pdf = Path(__file__).resolve().parents[1] / "sources/pdfs/Langchain - class48.pdf"
    with TemporaryDirectory(dir=Path(__file__).parent) as temp:
        folder = Path(temp)
        txt_path = folder / "rules.txt"
        txt_path.write_text("Students must carry ID cards.", encoding="utf-8")
        csv_path = folder / "students.csv"
        csv_path.write_text("name,course\nRavi,Python\nPriya,Java\n", encoding="utf-8")
        html_path = folder / "courses.html"
        html_path.write_text(
            "<html><title>Courses</title><main><h1>Course Updates</h1>"
            "<p>Python batch starts Monday.</p></main></html>",
            encoding="utf-8",
        )
        pdf_path = folder / "two_page_sample.pdf"
        original = PdfReader(str(source_pdf))
        writer = PdfWriter()
        for page in original.pages[:2]:
            writer.add_page(page)
        with pdf_path.open("wb") as stream:
            writer.write(stream)

        documents = [
            Document(
                page_content=txt_path.read_text(encoding="utf-8"),
                metadata={"source": str(txt_path), "source_type": "txt", "department": "Admin"},
            )
        ]
        for page_index, page in enumerate(PdfReader(str(pdf_path)).pages):
            documents.append(
                Document(
                    page_content=page.extract_text() or "",
                    metadata={
                        "source": str(pdf_path),
                        "source_type": "pdf",
                        "department": "HR",
                        "page": page_index,
                        "total_pages": 2,
                    },
                )
            )
        with csv_path.open("r", encoding="utf-8", newline="") as stream:
            for row_index, row in enumerate(csv.DictReader(stream)):
                documents.append(
                    Document(
                        page_content="\n".join(f"{key}: {value}" for key, value in row.items()),
                        metadata={
                            "source": str(csv_path),
                            "source_type": "csv",
                            "department": "Admissions",
                            "row": row_index,
                        },
                    )
                )
        soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
        documents.append(
            Document(
                page_content=soup.select_one("main").get_text(" ", strip=True),
                metadata={
                    "source": html_path.as_uri(),
                    "source_type": "html",
                    "department": "Training",
                    "title": soup.title.get_text(strip=True),
                },
            )
        )
        report = program_4_inspect(documents)
        return documents, report


if __name__ == "__main__":
    pdf = Document(page_content="Leave policy", metadata={"source": "policy.pdf", "page": 0})
    csv_document = Document(page_content="Ravi,Python", metadata={"source": "students.csv", "row": 1})
    enriched = program_1_enrich(pdf, "pdf", "policy")
    normalized = [program_3_standardize(item) for item in (enriched, csv_document)]
    assert normalized[0].metadata["display_page"] == 1
    assert normalized[1].metadata["display_row"] == 2
    for result in program_4_inspect(normalized):
        print(result)
    documents, report = program_4_multiformat_demo()
    assert len(documents) == 6
    assert {item["type"] for item in report} == {"txt", "pdf", "csv", "html"}
    print("Multi-format report:")
    for item in report:
        print(item)
