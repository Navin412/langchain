"""Class 12: requirements -> variables -> chat prompt -> model response."""

import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this live example.")
    destination = input("Destination: ").strip()
    days = input("Number of days: ").strip()
    budget = input("Budget and currency: ").strip()
    if not destination or not days.isdigit() or int(days) < 1 or not budget:
        raise SystemExit("Enter a destination, positive day count, and budget.")

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful travel planner. State assumptions clearly."),
        (
            "human",
            "Plan a {days}-day trip to {destination} with a budget of {budget}. "
            "Give a day-by-day outline, transport, food, and approximate costs. "
            "Do not claim current prices or availability without a live source.",
        ),
    ])
    answer = (prompt | ChatOpenAI(model="gpt-4o-mini")).invoke(
        {"destination": destination, "days": days, "budget": budget}
    )
    print(answer.content)


if __name__ == "__main__":
    main()
