"""Classes 73–74: split Documents, embed text, and retain metadata."""

import os

from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this API example")
    documents = [
        Document(
            page_content=(
                "Employees receive twelve casual leave days each year. "
                "Manager approval is required before taking leave."
            ),
            metadata={"source": "sample-policy.txt", "page": 1},
        )
    ]
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=80, chunk_overlap=15
    ).split_documents(documents)
    texts = [chunk.page_content for chunk in chunks]
    vectors = OpenAIEmbeddings(model="text-embedding-3-small").embed_documents(texts)
    assert len(chunks) == len(vectors)
    records = [
        {"text": chunk.page_content, "metadata": chunk.metadata, "vector": vector}
        for chunk, vector in zip(chunks, vectors)
    ]
    for record in records:
        print(record["metadata"], repr(record["text"]), "dimensions:", len(record["vector"]))
    print("Records are in memory only; this example does not save or index them.")


if __name__ == "__main__":
    main()
