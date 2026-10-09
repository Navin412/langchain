"""Route a topic to a beginner, intermediate, or advanced prompt."""

import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch
from langchain_openai import ChatOpenAI


def build_router(model: ChatOpenAI) -> RunnableBranch:
    parser = StrOutputParser()
    beginner = PromptTemplate.from_template(
        "Explain {topic} in simple English. Give a definition, five key points, and one example."
    ) | model | parser
    intermediate = PromptTemplate.from_template(
        "Explain {topic} with important concepts, a practical example, and common mistakes."
    ) | model | parser
    advanced = PromptTemplate.from_template(
        "Explain the architecture of {topic}, implementation choices, and interview questions."
    ) | model | parser
    return RunnableBranch(
        (lambda data: data["level"] == "beginner", beginner),
        (lambda data: data["level"] == "intermediate", intermediate),
        advanced,
    )


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this live example.")
    topic = input("Topic: ").strip()
    level = input("Level (beginner/intermediate/advanced): ").strip().lower()
    if not topic or level not in {"beginner", "intermediate", "advanced"}:
        raise SystemExit("Enter a topic and one of the three supported levels.")
    router = build_router(ChatOpenAI(model="gpt-4o-mini"))
    print(router.invoke({"topic": topic, "level": level}))


if __name__ == "__main__":
    main()
