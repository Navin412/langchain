"""Classes 64–66: compare recursive splitting settings without an API key."""

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def main() -> None:
    document = Document(
        page_content=(
            "Leave policy\nEmployees receive twelve casual leave days each year. "
            "Request approval from a manager.\n\n"
            "Security policy\nUse a strong password and report suspicious messages."
        ),
        metadata={"source": "sample-policy.txt", "page": 1},
    )
    for size, overlap in ((50, 0), (80, 15)):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=size,
            chunk_overlap=overlap,
            separators=["\n\n", "\n", " ", ""],
            add_start_index=True,
        )
        chunks = splitter.split_documents([document])
        print(f"\nsize={size}, overlap={overlap}, chunks={len(chunks)}")
        for chunk in chunks:
            assert chunk.metadata["source"] == document.metadata["source"]
            print(repr(chunk.page_content), chunk.metadata)


if __name__ == "__main__":
    main()
