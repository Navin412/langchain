"""Class 10: compare Python fallback values with PromptTemplate.partial()."""

from langchain_core.prompts import PromptTemplate


def main() -> None:
    topic = input("Topic (default Python): ").strip() or "Python"
    level = input("Level (default beginner): ").strip() or "beginner"

    template = PromptTemplate.from_template("Explain {topic} at the {level} level.")
    print("Python defaults:", template.invoke({"topic": topic, "level": level}).to_string())

    partial = template.partial(level="beginner")
    print("Partial default:", partial.invoke({"topic": topic}).to_string())
    print("Explicit override:", partial.invoke({"topic": topic, "level": "advanced"}).to_string())


if __name__ == "__main__":
    main()
