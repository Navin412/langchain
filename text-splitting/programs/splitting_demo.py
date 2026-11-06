"""Class 62: separator splitting, document metadata, and an oversized piece."""

from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter


def main() -> None:
    splitter = CharacterTextSplitter(separator="|", chunk_size=7, chunk_overlap=0)
    print("Strings:", splitter.split_text("AAA|BBB|CCC|DDD"))

    document = Document(page_content="AAA|BBB|CCC|DDD", metadata={"source": "demo.txt"})
    chunks = splitter.split_documents([document])
    print("Documents:", [(item.page_content, item.metadata) for item in chunks])
    assert all(item.metadata["source"] == "demo.txt" for item in chunks)

    long_piece = "A" * 12
    print("No separator to cut at:", splitter.split_text(long_piece))
    recursive = RecursiveCharacterTextSplitter(chunk_size=7, chunk_overlap=0)
    print("With fallback separators:", recursive.split_text(long_piece))


if __name__ == "__main__":
    main()
