"""Class 38: LCEL chat with separate in-memory conversation sessions."""

import os

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI


store: dict[str, InMemoryChatMessageHistory] = {}


def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a concise, helpful study assistant."),
    MessagesPlaceholder("history"),
    ("human", "{question}"),
])


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this live example.")

    chain = prompt | ChatOpenAI(model="gpt-4o-mini")
    chat = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="question",
        history_messages_key="history",
    )
    print("Use a unique conversation ID. Type exit as the question to stop.")
    while True:
        session_id = input("Conversation ID: ").strip()
        if not session_id:
            print("Conversation ID cannot be empty.")
            continue
        question = input("You: ").strip()
        if question.lower() == "exit":
            break
        if not question:
            continue
        answer = chat.invoke(
            {"question": question},
            config={"configurable": {"session_id": session_id}},
        )
        print(f"AI: {answer.content}")


if __name__ == "__main__":
    main()
