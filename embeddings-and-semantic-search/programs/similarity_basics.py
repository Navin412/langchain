"""Classes 69–70: word overlap and cosine similarity, offline."""

from math import sqrt


def jaccard(left: str, right: str) -> float:
    a, b = set(left.lower().split()), set(right.lower().split())
    return len(a & b) / len(a | b) if a | b else 0.0


def cosine(left: list[float], right: list[float]) -> float:
    if len(left) != len(right):
        raise ValueError("Vectors must have matching dimensions")
    left_length = sqrt(sum(x * x for x in left))
    right_length = sqrt(sum(x * x for x in right))
    if not left_length or not right_length:
        raise ValueError("Cosine similarity is undefined for a zero vector")
    return sum(x * y for x, y in zip(left, right)) / (left_length * right_length)


def main() -> None:
    question = "How many days can staff take off?"
    policy = "Employees receive twelve casual leave days each year."
    print("Word-overlap score:", round(jaccard(question, policy), 3))
    print("Similar manual vectors:", round(cosine([1, 2, 3], [2, 3, 4]), 3))
    print("Orthogonal vectors:", round(cosine([1, 0], [0, 1]), 3))
    print("Manual vectors illustrate the formula; they are not semantic embeddings.")


if __name__ == "__main__":
    main()
