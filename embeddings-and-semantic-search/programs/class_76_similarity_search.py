"""Seven Class 76 PDF exercises in vector similarity and semantic search."""

import argparse
import os
from math import dist, sqrt

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from similarity_basics import cosine


def metric_exercises() -> None:
    # 1. Calculate cosine similarity from the dot product and magnitudes.
    left, right = [1, 0], [0.8, 0.6]
    dot = sum(a * b for a, b in zip(left, right))
    left_length = sqrt(sum(value ** 2 for value in left))
    right_length = sqrt(sum(value ** 2 for value in right))
    print(f"1. Dot product: {dot}, magnitudes: {left_length}, {right_length}")
    print(f"   Cosine similarity: {dot / (left_length * right_length):.2f}")

    # 2. Use the reusable helper for similar, perpendicular, and opposite vectors.
    scores = [round(cosine(left, vector), 2) for vector in (right, [0, 1], [-1, 0])]
    print(f"2. Cosine scores: {scores}")

    # 3. Compare all three metrics on vectors with the same direction.
    right = [2, 0]
    dot = sum(a * b for a, b in zip(left, right))
    print(f"3. Dot: {dot}, cosine: {cosine(left, right):.2f}, distance: {dist(left, right):.2f}")


def rank_documents(
    question: str, documents: list[Document], embeddings: Embeddings
) -> list[tuple[float, Document]]:
    if not question.strip():
        raise ValueError("Question cannot be empty")
    if not documents:
        return []

    vectors = embeddings.embed_documents([document.page_content for document in documents])
    query_vector = embeddings.embed_query(question)
    scored = [
        (cosine(query_vector, vector), document)
        for document, vector in zip(documents, vectors, strict=True)
    ]
    return sorted(scored, key=lambda result: result[0], reverse=True)


def show_results(results: list[tuple[float, Document]]) -> None:
    for rank, (score, document) in enumerate(results, start=1):
        source = document.metadata.get("source", "")
        category = document.metadata.get("category", "")
        provenance = f" [{source}, {category}]" if source else ""
        print(f"   {rank}. {score:.4f}  {document.page_content}{provenance}")


def embedding_exercises(embeddings: Embeddings, question: str, top_k: int) -> None:
    # 4. Compare related sentences with an unrelated sentence.
    anchor = embeddings.embed_query("I want to learn Python.")
    related = embeddings.embed_query("How can I study Python programming?")
    unrelated = embeddings.embed_query("The weather is very hot today.")
    print(f"4. Related: {cosine(anchor, related):.4f}, unrelated: {cosine(anchor, unrelated):.4f}")

    # 5–6. Rank the same batch once, then take the top K without re-embedding.
    documents = [
        Document(page_content=text)
        for text in (
            "Python is a programming language.",
            "Employees can work remotely.",
            "The library closes at 6 PM.",
            "Staff members can perform their jobs from home.",
            "Students can attend online training.",
        )
    ]
    ranked = rank_documents("Can employees work from home?", documents, embeddings)
    print("5. All documents ranked:")
    show_results(ranked)
    print(f"6. Top {top_k} documents:")
    show_results(ranked[:top_k])

    # 7. Split the course knowledge base and retain metadata in retrieved chunks.
    course_records = [
        ("python_course.txt", "Courses", "Python training is available for beginners and experienced developers."),
        ("java_course.txt", "Courses", "Java training covers object-oriented programming and enterprise development."),
        ("online_classes.txt", "Learning", "Students can attend live online classes from home."),
        ("recordings.txt", "Learning", "Registered students can access recorded sessions under their course access terms."),
        ("fees.txt", "Support", "Students can contact the support team for course fee information."),
        ("support.txt", "Support", "The support team helps with course access and technical issues."),
    ]
    course_documents = [
        Document(page_content=text, metadata={"source": source, "category": category})
        for source, category, text in course_records
    ]
    splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=20)
    chunks = splitter.split_documents(course_documents)
    print(f"7. Matching course chunks for {question!r}:")
    show_results(rank_documents(question, chunks, embeddings)[:top_k])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="Run exercises 4–7 using OpenAI")
    parser.add_argument("--question", default="Can I attend classes from home?")
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()
    if args.top_k < 1:
        parser.error("--top-k must be positive")
    if not args.question.strip():
        parser.error("--question cannot be empty")
    if args.live and not os.getenv("OPENAI_API_KEY"):
        parser.error("Set OPENAI_API_KEY before using --live")

    metric_exercises()
    if args.live:
        from langchain_openai import OpenAIEmbeddings

        embedding_exercises(OpenAIEmbeddings(model="text-embedding-3-small"), args.question, args.top_k)
    else:
        print("Use --live with OPENAI_API_KEY to run exercises 4–7.")


if __name__ == "__main__":
    main()
