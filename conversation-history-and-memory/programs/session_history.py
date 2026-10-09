"""Class 37: session-isolated chat history without an external model."""

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables.history import RunnableWithMessageHistory


store: dict[str, InMemoryChatMessageHistory] = {}


def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


def reply(messages: list[BaseMessage]) -> AIMessage:
    latest = next(
        message.content for message in reversed(messages)
        if isinstance(message, HumanMessage)
    )
    return AIMessage(content=f"Received: {latest} (messages seen: {len(messages)})")


chat = RunnableWithMessageHistory(RunnableLambda(reply), get_session_history)


if __name__ == "__main__":
    for session_id, question in [
        ("conversation-a", "Hello"),
        ("conversation-a", "What did I say before?"),
        ("conversation-b", "Hello from another conversation"),
    ]:
        answer = chat.invoke(
            [HumanMessage(content=question)],
            config={"configurable": {"session_id": session_id}},
        )
        print(f"{session_id}: {answer.content}")
    print({session_id: len(history.messages) for session_id, history in store.items()})
