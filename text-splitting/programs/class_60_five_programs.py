"""Five offline practice programs for Class 60 text-splitting concepts.

These are runnable adaptations of the five programs in the ChatGPT study note.
They are not a verbatim copy of the classroom PDF.
"""

from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter


def fixed_size_chunks(text: str, size: int) -> list[str]:
    """Program 1: plain Python fixed-size chunking, without overlap."""
    if size <= 0:
        raise ValueError("size must be positive")
    return [text[index : index + size] for index in range(0, len(text), size)]


def overlapping_chunks(text: str, size: int, overlap: int) -> list[str]:
    """Program 2: plain Python chunks that repeat neighboring characters."""
    if size <= 0 or not 0 <= overlap < size:
        raise ValueError("require size > 0 and 0 <= overlap < size")
    step = size - overlap
    return [text[index : index + size] for index in range(0, len(text), step)]


def separator_parts(text: str, separator: str) -> list[str]:
    """Program 3: inspect the pieces before a LangChain splitter merges them."""
    return text.split(separator)


def langchain_chunks(text: str) -> list[str]:
    """Program 4: use CharacterTextSplitter on a string."""
    splitter = CharacterTextSplitter(separator="|", chunk_size=7, chunk_overlap=0)
    return splitter.split_text(text)


def document_chunks(document: Document) -> list[Document]:
    """Program 5: split a Document and carry its metadata into each chunk."""
    splitter = CharacterTextSplitter(separator="|", chunk_size=7, chunk_overlap=0)
    return splitter.split_documents([document])


if __name__ == "__main__":
    print("1. Fixed size:", fixed_size_chunks("ABCDEFGHIJKL", 5))
    print("2. Overlap:", overlapping_chunks("ABCDEFGHIJKL", 5, 2))
    print("3. Separator parts:", separator_parts("AAA|BBB|CCC|DDD", "|"))
    print("4. LangChain chunks:", langchain_chunks("AAA|BBB|CCC|DDD"))
    source = Document(page_content="AAA|BBB|CCC|DDD", metadata={"source": "demo.txt"})
    chunks = document_chunks(source)
    print("5. Document chunks:", [(item.page_content, item.metadata) for item in chunks])
    assert all(item.metadata["source"] == "demo.txt" for item in chunks)
