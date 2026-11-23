"""Class 69: five vector fundamentals from the PDF, without API calls."""

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from similarity_basics import cosine


def main() -> None:
    # 1. Inspect a manually entered vector.
    vector = [0.12, -0.35, 0.78, 0.41]
    print("1. Vector:", vector, "type:", type(vector).__name__, "dimensions:", len(vector))
    for dimension, value in enumerate(vector, start=1):
        print(f"   Dimension {dimension}: {value}")

    # 2. Text is a string; these sample numbers are not its embedding.
    text = "Python is a programming language."
    print("2. Text and manual vector:", type(text).__name__, type(vector).__name__)

    # 3. Dimensions must match before vector comparison.
    vectors = ([0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8])
    print("3. Dimensions:", [len(v) for v in vectors])
    assert len(vectors[0]) == len(vectors[1]) != len(vectors[2])

    # 4. Split a Document into chunks; no embeddings are generated yet.
    doc = Document(
        page_content=(
            "Python is a popular programming language. "
            "Java is widely used in enterprise applications. "
            "LangChain helps build applications using LLMs."
        ),
        metadata={"source": "courses.txt"},
    )
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=55, chunk_overlap=0
    ).split_documents([doc])
    print("4. Chunks:", [(c.page_content, c.metadata) for c in chunks])

    # 5. Cosine similarity for manually entered vectors.
    print("5. Similarity:", round(cosine([1, 0], [0.8, 0.6]), 2))
    print("5. Orthogonal:", round(cosine([1, 0], [0, 1]), 2))
    print("Manual vectors demonstrate the math, not semantic meaning.")


if __name__ == "__main__":
    main()
