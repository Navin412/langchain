"""Continue a chat after restarting Python using a JSON file per session."""

import os
from pathlib import Path

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

from file_chat_history import FileChatMessageHistory


HISTORY_DIRECTORY = Path(__file__).resolve().parents[2] / "chat_history"


def get_session_history(session_id: str) -> FileChatMessageHistory:
    return FileChatMessageHistory(session_id, HISTORY_DIRECTORY)


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this live example.")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. Answer in simple English."),
        MessagesPlaceholder("history"),
        ("human", "{question}"),
    ])
    chatbot = RunnableWithMessageHistory(
        prompt | ChatOpenAI(model="gpt-4o-mini"),
        get_session_history,
        input_messages_key="question",
        history_messages_key="history",
    )
    session_id = input("Conversation ID: ").strip()
    if not session_id:
        raise SystemExit("Conversation ID cannot be empty.")
    print("Type exit to stop. Reuse this ID after restarting to load its history.")
    while True:
        question = input("You: ").strip()
        if question.lower() == "exit":
            break
        if not question:
            continue
        answer = chatbot.invoke(
            {"question": question},
            config={"configurable": {"session_id": session_id}},
        )
        print("AI:", answer.content)


if __name__ == "__main__":
    main()
