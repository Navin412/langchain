"""Class 58: metadata enrichment, page/row labels, normalization and inspection.

Run: python practice/class58_metadata.py
"""

from langchain_core.documents import Document


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


if __name__ == "__main__":
    pdf = Document(page_content="Leave policy", metadata={"source": "policy.pdf", "page": 0})
    csv = Document(page_content="Ravi,Python", metadata={"source": "students.csv", "row": 1})
    enriched = program_1_enrich(pdf, "pdf", "policy")
    normalized = [program_3_standardize(item) for item in (enriched, csv)]
    assert normalized[0].metadata["display_page"] == 1
    assert normalized[1].metadata["display_row"] == 2
    for result in program_4_inspect(normalized):
        print(result)
