"""Eight offline practice programs for Class 62 CharacterTextSplitter.

These follow the eight topics in the ChatGPT study note. Exact chunk output can
vary with separator and installed text-splitter version, so each example prints
its result rather than assuming every setting produces fixed-width chunks.
"""

from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter


def show(label: str, chunks: list[str] | list[Document]) -> None:
    print(f"{label}: {chunks}")


def main() -> None:
    text = "AAA|BBB|CCC|DDD"

    # 1. First CharacterTextSplitter program: split, then merge pieces.
    basic = CharacterTextSplitter(separator="|", chunk_size=7, chunk_overlap=0)
    show("1. First splitter", basic.split_text(text))

    # 2. Default separator: a newline. No newline means no place to split.
    default_separator = CharacterTextSplitter(chunk_size=7, chunk_overlap=0)
    show("2. Default separator", default_separator.split_text(text))

    # 3. A missing configured separator may leave an oversized chunk.
    show("3. Missing separator", basic.split_text("ABCDEFGHIJKL"))

    # 4. Use spaces as split points between words.
    words = CharacterTextSplitter(separator=" ", chunk_size=12, chunk_overlap=0)
    show("4. Space separator", words.split_text("red green blue yellow"))

    # 5. Overlap can repeat text between neighboring chunks.
    overlap = CharacterTextSplitter(separator=" ", chunk_size=14, chunk_overlap=5)
    overlapping = overlap.split_text("one two three four five six seven")
    show("5. Chunk overlap", overlapping)
    assert "three" in overlapping[0] and "three" in overlapping[1]

    # 6. Observe what happens when a separator is retained or dropped.
    for keep in (False, True):
        splitter = CharacterTextSplitter(
            separator="|", chunk_size=7, chunk_overlap=0, keep_separator=keep
        )
        show(f"6. keep_separator={keep}", splitter.split_text(text))

    # 7. split_documents() carries source metadata into the output Documents.
    document = Document(page_content=text, metadata={"source": "lesson.txt"})
    pieces = basic.split_documents([document])
    show("7. Split Documents", pieces)
    assert all(piece.metadata["source"] == "lesson.txt" for piece in pieces)

    # 8. add_start_index records the chunk's starting character position.
    indexed = CharacterTextSplitter(
        separator="|", chunk_size=7, chunk_overlap=0, add_start_index=True
    )
    indexed_pieces = indexed.split_documents([document])
    show("8. Start indexes", indexed_pieces)
    assert all("start_index" in piece.metadata for piece in indexed_pieces)


if __name__ == "__main__":
    main()
