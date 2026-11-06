"""Class 58: preserve source metadata and inspect document readiness."""

from langchain_core.documents import Document


def standardize(document: Document, source_type: str, category: str) -> Document:
    document.metadata.update({"source_type": source_type, "category": category})
    return document


def report(documents: list[Document]) -> None:
    for index, document in enumerate(documents, start=1):
        ready = bool(document.page_content.strip()) and bool(document.metadata.get("source"))
        print(
            f"{index}: {'ready' if ready else 'check'} | "
            f"{document.metadata.get('source_type', '?')} | "
            f"{document.metadata.get('source', '?')} | "
            f"{document.page_content[:60]!r}"
        )


if __name__ == "__main__":
    docs = [
        Document(page_content="Leave policy: 12 days", metadata={"source": "policy.txt"}),
        Document(page_content="", metadata={"source": "scanned.pdf", "page": 0}),
    ]
    standardize(docs[0], "txt", "policy")
    standardize(docs[1], "pdf", "policy")
    assert docs[1].metadata["page"] == 0
    report(docs)
