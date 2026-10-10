"""Class 41: compare in-memory and JSON-file chat history without an API key.

Run from any directory with the repository requirements installed. Restarting a
Python process clears the in-memory dictionary; reopening the JSON file does not.
"""

import argparse
from contextlib import nullcontext
from pathlib import Path
from tempfile import TemporaryDirectory

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables.history import RunnableWithMessageHistory

from file_chat_history import FileChatMessageHistory


def reply(messages: list[BaseMessage]) -> AIMessage:
    """Expose how many earlier messages the model receives."""
    return AIMessage(content=f"Messages received: {len(messages)}")


def ask(chat: RunnableWithMessageHistory, question: str) -> str:
    answer = chat.invoke(
        [HumanMessage(content=question)],
        config={"configurable": {"session_id": "class-41-demo"}},
    )
    return str(answer.content)


def main(storage_dir: Path | None = None) -> None:
    memory: dict[str, InMemoryChatMessageHistory] = {}

    def in_memory(session_id: str) -> InMemoryChatMessageHistory:
        return memory.setdefault(session_id, InMemoryChatMessageHistory())

    memory_chat = RunnableWithMessageHistory(RunnableLambda(reply), in_memory)
    print("In memory, first:", ask(memory_chat, "Hello"))
    print("In memory, second:", ask(memory_chat, "Again"))
    memory.clear()  # Simulate a process restart.
    print("In memory, after restart:", ask(memory_chat, "Do you remember?"))

    storage = TemporaryDirectory() if storage_dir is None else nullcontext(str(storage_dir))
    with storage as directory:
        def file_history(session_id: str) -> FileChatMessageHistory:
            return FileChatMessageHistory(session_id, directory)

        file_chat = RunnableWithMessageHistory(RunnableLambda(reply), file_history)
        print("File, first:", ask(file_chat, "Hello"))
        print("File, second:", ask(file_chat, "Again"))
        # Rebuild the wrapper and history object, as a fresh process would.
        reopened = RunnableWithMessageHistory(RunnableLambda(reply), file_history)
        print("File, after reopening:", ask(reopened, "Do you remember?"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--storage-dir", type=Path, help="Use an existing directory for the JSON demo")
    args = parser.parse_args()
    main(args.storage_dir)
