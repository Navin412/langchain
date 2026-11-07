"""Export searchable page text from the archived numbered class PDFs.

Run from the repository root: python practice/export_pdf_text.py
The output is reference text, not executable Python. PDF text extraction can
change spacing and cannot read code that exists only as an image.
"""

import re
from pathlib import Path
from urllib.parse import quote

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources" / "pdfs"
OUTPUT = ROOT / "practice" / "pdf-text"


def export() -> list[tuple[int, str, int]]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    results = []
    files = []
    for pdf in SOURCE.glob("*.pdf"):
        match = re.search(r"class\s*(\d+)", pdf.name, re.IGNORECASE)
        if match:
            files.append((int(match.group(1)), pdf))
    for number, pdf in sorted(files):
        reader = PdfReader(pdf)
        lines = [
            f"# Class {number}: searchable PDF text",
            "",
            f"Source: [original PDF](../../sources/pdfs/{quote(pdf.name)})",
            "",
            "This is raw text from the PDF's text layer, kept by page for searching and copying. "
            "It is not a checked Python program. For runnable exercises, use "
            "the [practice guide](../README.md). Consult the PDF for layout, images and exact code.",
            "",
        ]
        for page_number, page in enumerate(reader.pages, 1):
            extracted = page.extract_text(extraction_mode="layout") or ""
            lines.extend(
                [
                    f"## Page {page_number}",
                    "",
                    "~~~~text",
                    extracted.rstrip(),
                    "~~~~",
                    "",
                ]
            )
        (OUTPUT / f"class{number:02d}.md").write_text("\n".join(lines), encoding="utf-8")
        results.append((number, pdf.name, len(reader.pages)))
    index = [
        "# Searchable class PDF text",
        "",
        "Each link contains the extracted text from every page of the numbered class PDF. "
        "Use these files to search or copy examples; the [practice guide](../README.md) "
        "links runnable adaptations. Extraction can alter spacing and cannot recover text "
        "that was embedded only as an image. The original PDFs are linked on every page.",
        "",
        "| Class | Searchable text | Original PDF | Pages |",
        "| --- | --- | --- | ---: |",
    ]
    for number, filename, pages in results:
        index.append(
            f"| {number} | [Class {number}](class{number:02d}.md) | "
            f"[PDF](../../sources/pdfs/{quote(filename)}) | {pages} |"
        )
    (OUTPUT / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    return results


if __name__ == "__main__":
    results = export()
    print(f"Exported {len(results)} numbered PDFs to {OUTPUT}")
