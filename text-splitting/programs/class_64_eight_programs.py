"""Class 64: eight RecursiveCharacterTextSplitter exercises, adapted from the PDF."""

from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter


def show(label: str, value: object) -> None:
    print(f"\n{label}: {value}")


def main() -> None:
    # 1. Fall back to individual characters when no natural separator exists.
    text = "ABCDEFGHIJKL"
    recursive = RecursiveCharacterTextSplitter(chunk_size=5, chunk_overlap=0)
    show("1. First recursive split", recursive.split_text(text))

    # 2. A single missing separator leaves one oversized CharacterTextSplitter piece.
    character = CharacterTextSplitter(separator="\n\n", chunk_size=5, chunk_overlap=0)
    show("2. Character vs recursive", (character.split_text(text), recursive.split_text(text)))

    # 3. Custom separator priority.
    custom = RecursiveCharacterTextSplitter(
        separators=["|", ""], chunk_size=7, chunk_overlap=0, keep_separator=False
    )
    show("3. Custom separators", custom.split_text("AAA|BBB|CCC|DDD"))

    # 4. An oversized piece falls back from '|' to characters.
    deeper = RecursiveCharacterTextSplitter(
        separators=["|", ""], chunk_size=5, chunk_overlap=0, keep_separator=False
    )
    show("4. Deeper fallback", deeper.split_text("AAA|ABCDEFGHIJ|BBB"))

    # 5. Neighboring chunks can repeat characters.
    overlap = RecursiveCharacterTextSplitter(
        separators=[""], chunk_size=5, chunk_overlap=2
    )
    show("5. Overlap", overlap.split_text(text))

    # 6. Retain the separator at the start of the following piece.
    retained = RecursiveCharacterTextSplitter(
        separators=["|", ""], chunk_size=4, chunk_overlap=0, keep_separator="start"
    )
    show("6. keep_separator", retained.split_text("AAA|BBB|CCC"))

    # 7. split_documents carries source metadata into each chunk.
    doc = Document(page_content=text, metadata={"source": "company_policy.txt", "department": "HR"})
    chunks = recursive.split_documents([doc])
    assert all(chunk.metadata["department"] == "HR" for chunk in chunks)
    show("7. Document metadata", [(c.page_content, c.metadata) for c in chunks])

    # 8. More natural policy text with paragraph and line boundaries.
    policy = Document(
        page_content=(
            "ATTENDANCE POLICY\nEmployees must report by 9 AM.\n\n"
            "LEAVE POLICY\nEmployees receive 12 casual leaves.\n\n"
            "WORK FROM HOME\nManager approval is required."
        ),
        metadata={"source": "company_policy.txt"},
    )
    policy_chunks = RecursiveCharacterTextSplitter(
        chunk_size=60, chunk_overlap=10, add_start_index=True
    ).split_documents([policy])
    show("8. Company policy", [(c.page_content, c.metadata) for c in policy_chunks])


if __name__ == "__main__":
    main()
