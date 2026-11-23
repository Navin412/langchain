"""Class 74: seven document-embedding exercises from the PDF.

Requires OPENAI_API_KEY and calls the embedding API. Records stay in memory.
"""

import os

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def run(embeddings: object) -> None:
    # 1. Embed multiple text strings in one call.
    texts = ["Python is a programming language.", "Java runs on a JVM."]
    vectors = embeddings.embed_documents(texts)
    print("1. Texts and vectors:", len(texts), len(vectors))

    # 2. The query method accepts one string; the document method accepts a list.
    question = "Which language runs on a JVM?"
    query_vector = embeddings.embed_query(question)
    print("2. Query/document dimensions:", len(query_vector), [len(v) for v in vectors])

    # 3. Extract page_content before passing Document objects to embed_documents.
    documents = [
        Document(page_content=texts[0], metadata={"source": "courses.txt", "page": 1}),
        Document(page_content=texts[1], metadata={"source": "courses.txt", "page": 2}),
    ]
    document_vectors = embeddings.embed_documents([doc.page_content for doc in documents])
    print("3. Document objects embedded:", len(document_vectors))

    # 4. Split before embedding when source text is long.
    policy = Document(
        page_content=(
            "Employees receive twelve casual leave days each year. "
            "Manager approval is required before taking leave. "
            "Report suspicious messages to the security team."
        ),
        metadata={"source": "sample-policy.txt", "page": 1},
    )
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=80, chunk_overlap=15
    ).split_documents([policy])
    chunk_vectors = embeddings.embed_documents([chunk.page_content for chunk in chunks])
    print("4. Chunk count:", len(chunks))

    # 5. Check counts and a consistent vector size before using records.
    assert len(chunk_vectors) == len(chunks)
    dimensions = {len(vector) for vector in chunk_vectors}
    assert len(dimensions) == 1
    print("5. Vector dimensions:", dimensions.pop())

    # 6. Preserve text and metadata alongside each vector.
    records = [
        {"text": chunk.page_content, "metadata": chunk.metadata, "vector": vector}
        for chunk, vector in zip(chunks, chunk_vectors)
    ]
    print("6. Record sources:", [r["metadata"]["source"] for r in records])

    # 7. Complete in-memory preparation, without claiming a vector database exists.
    print("7. Prepared records:", len(records))
    print("No vector database was created; records were not persisted.")


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this API example")
    from langchain_openai import OpenAIEmbeddings

    run(OpenAIEmbeddings(model="text-embedding-3-small"))


if __name__ == "__main__":
    main()
