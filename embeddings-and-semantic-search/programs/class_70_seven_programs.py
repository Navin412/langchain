"""Class 70: seven offline keyword, Jaccard, and search-flow demonstrations."""

from similarity_basics import jaccard


def main() -> None:
    # 1. Exact substring matching misses a related word.
    document = "Employees can work remotely."
    print("1. 'home' found:", "home" in document.lower())

    # 2. Related questions can use different words.
    questions = [
        "Can employees work remotely?",
        "Can staff work from home?",
        "Are workers allowed to do their jobs from home?",
    ]
    print("2. Literal matches:", ["remotely" in q.lower() for q in questions])

    # 3. Jaccard measures word overlap; it does not infer meaning.
    print("3. Jaccard:", round(jaccard("I want to learn Python", "I want to study Python"), 2))

    # 4. Remove the uninformative article in the PDF's synonym example.
    stop_words = {"a", "the"}
    first = set("Purchase a vehicle".lower().split()) - stop_words
    second = set("Buy a car".lower().split()) - stop_words
    print("4. Synonym word overlap:", len(first & second) / len(first | second))

    # 5. A shared keyword does not resolve a word's meaning.
    sentences = [
        "Java is a programming language",
        "Java is an island in Indonesia",
        "Java is used for backend development",
    ]
    print("5. Java matches:", [s for s in sentences if "java" in s.lower()])

    # 6. A hand-written synonym map is only a simulation, not an embedding model.
    documents = {"remote_work": document, "online_training": "Students attend online classes."}
    concepts = {"remote_work": ["work remotely", "work from home"]}
    question = "Can I work from home?"
    matched = next(
        (documents[k] for k, phrases in concepts.items() if any(p in question.lower() for p in phrases)),
        None,
    )
    print("6. Manual lookup:", matched)

    # 7. Outline a vector-search pipeline without pretending to run one.
    print("7. Search flow: documents -> document vectors -> query vector -> scores -> results")
    print("No semantic embeddings or search scores were generated here.")


if __name__ == "__main__":
    main()
