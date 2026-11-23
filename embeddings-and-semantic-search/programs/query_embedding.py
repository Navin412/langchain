"""Class 72: generate one real embedding (requires OPENAI_API_KEY)."""

import os

from langchain_openai import OpenAIEmbeddings


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this API example")
    model = OpenAIEmbeddings(model="text-embedding-3-small")
    vector = model.embed_query("I am learning LangChain.")
    print("Dimensions:", len(vector))
    print("First five components:", [round(value, 4) for value in vector[:5]])


if __name__ == "__main__":
    main()
