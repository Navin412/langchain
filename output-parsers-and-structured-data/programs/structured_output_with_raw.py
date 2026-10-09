"""Inspect parsed output, raw AIMessage, and any parsing error (class 17)."""

import os
from typing import Literal

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class SupportTicket(BaseModel):
    category: Literal["billing", "technical", "account", "other"]
    priority: Literal["low", "medium", "high"]
    summary: str = Field(description="One-sentence account of the customer's issue")


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this live example.")
    model = ChatOpenAI(model="gpt-4o-mini")
    extractor = model.with_structured_output(SupportTicket, include_raw=True)
    result = extractor.invoke("My payment failed and I cannot access my account. Please help.")
    if result["parsing_error"] is not None:
        raise RuntimeError(f"Could not parse model output: {result['parsing_error']}")
    ticket: SupportTicket = result["parsed"]
    print("Raw response:", result["raw"])
    print("Validated ticket:", ticket.model_dump())
    # A valid schema gives the right shape; review the facts before acting on them.


if __name__ == "__main__":
    main()
