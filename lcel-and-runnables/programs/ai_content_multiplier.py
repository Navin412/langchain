"""Create one explanation, then make independent outputs from it."""

import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI


def build_chain(model: ChatOpenAI):
    parser = StrOutputParser()
    explanation = PromptTemplate.from_template(
        "Explain {topic} for {audience}. Give a definition, five points, and an example."
    ) | model | parser
    branches = RunnableParallel(
        explanation=RunnablePassthrough(),
        summary=PromptTemplate.from_template(
            "Summarize in five short bullets:\n{content}"
        ) | model | parser,
        quiz=PromptTemplate.from_template(
            "Write five beginner multiple-choice questions with answers based only on:\n{content}"
        ) | model | parser,
        social_post=PromptTemplate.from_template(
            "Write a short social media post based on:\n{content}"
        ) | model | parser,
        interview_questions=PromptTemplate.from_template(
            "Write five beginner interview questions based on:\n{content}"
        ) | model | parser,
    )
    return (
        explanation
        | RunnableLambda(lambda content: {"content": content})
        | branches
        | RunnableLambda(lambda result: {**result, "explanation": result["explanation"]["content"]})
    )


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this live example.")
    topic = input("Topic: ").strip()
    audience = input("Audience: ").strip()
    if not topic or not audience:
        raise SystemExit("Both topic and audience are required.")
    result = build_chain(ChatOpenAI(model="gpt-4o-mini")).invoke(
        {"topic": topic, "audience": audience}
    )
    for name, content in result.items():
        print(f"\n{name.upper()}\n{content}")


if __name__ == "__main__":
    main()
