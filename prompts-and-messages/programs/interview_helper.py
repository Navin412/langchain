"""Class 12: generate tailored interview practice from a reusable chat prompt."""

import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this live example.")
    technology = input("Technology: ").strip()
    level = input("Level (beginner/intermediate/advanced): ").strip().lower()
    if not technology or level not in {"beginner", "intermediate", "advanced"}:
        raise SystemExit("Enter a technology and a supported level.")

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a practical technical interviewer."),
        (
            "human",
            "Create five {level} interview questions about {technology}. "
            "For each, give a concise model answer and one common mistake.",
        ),
    ])
    answer = (prompt | ChatOpenAI(model="gpt-4o-mini")).invoke(
        {"technology": technology, "level": level}
    )
    print(answer.content)


if __name__ == "__main__":
    main()
