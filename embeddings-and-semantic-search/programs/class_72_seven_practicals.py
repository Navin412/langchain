"""Class 72: seven embedding-model practicals from the PDF.

The first six use OpenAI and incur API calls. Pass --local to run the seventh
with the optional langchain-huggingface package and a local model download.
"""

import argparse
import os

from similarity_basics import cosine


def cloud_practicals() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running cloud embedding practicals")
    from langchain_openai import OpenAIEmbeddings

    model = OpenAIEmbeddings(model="text-embedding-3-small")

    # 1. One query string becomes one vector.
    first = model.embed_query("I am learning LangChain.")
    print("1. First embedding:", type(first).__name__, len(first), first[:5])

    # 2. Several sentences, always from the same model.
    sentences = ["I like Python.", "Python programming is fun.", "The sky is blue."]
    vectors = model.embed_documents(sentences)
    print("2. Sentence dimensions:", [len(v) for v in vectors])

    # 3. Input length does not set this model's vector dimensions.
    long_text = "LangChain helps build applications. " * 5
    long_vector = model.embed_query(long_text)
    print("3. Short vs long dimensions:", len(first), len(long_vector))

    # 4. The text-embedding-3 family supports a shorter requested vector.
    smaller = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=256)
    short_vector = smaller.embed_query("LangChain helps build applications.")
    print("4. Requested dimensions:", len(short_vector))
    assert len(short_vector) == 256

    # 5. Cosine comparison only among vectors from the same model/configuration.
    print("5. Related score:", round(cosine(vectors[0], vectors[1]), 3))
    print("5. Different-topic score:", round(cosine(vectors[0], vectors[2]), 3))

    # 6. Inspect type and a small sample, not the whole vector.
    print("6. Component type:", type(first[0]).__name__, "sample:", first[:3])


def local_practical() -> None:
    try:
        from langchain_huggingface import HuggingFaceEmbeddings
    except ImportError as exc:
        raise SystemExit(
            "Install optional langchain-huggingface and sentence-transformers packages"
        ) from exc
    model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector = model.embed_query("I am learning LangChain.")
    print("7. Local model dimensions:", len(vector), "sample:", vector[:5])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local", action="store_true", help="Run only the optional local-model exercise")
    args = parser.parse_args()
    if args.local:
        local_practical()
    else:
        cloud_practicals()


if __name__ == "__main__":
    main()
