"""A small JSON-backed BaseChatMessageHistory for one conversation ID.

Educational file store. For concurrent writers or many users, use a database-backed
store with access controls and appropriate retention.
"""

import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Sequence

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage, message_to_dict, messages_from_dict


class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id: str, storage_path: str | Path = "chat_history") -> None:
        if not session_id:
            raise ValueError("session_id cannot be empty")
        directory = Path(storage_path)
        directory.mkdir(parents=True, exist_ok=True)
        # Hash the ID so user input cannot become a filesystem path.
        filename = hashlib.sha256(session_id.encode("utf-8")).hexdigest() + ".json"
        self.file_path = directory / filename

    @property
    def messages(self) -> list[BaseMessage]:
        if not self.file_path.exists():
            return []
        with self.file_path.open("r", encoding="utf-8") as file:
            return messages_from_dict(json.load(file))

    def _write(self, messages: Sequence[BaseMessage]) -> None:
        # Replace the complete file only after the new JSON has been written.
        handle, temp_name = tempfile.mkstemp(dir=self.file_path.parent, suffix=".tmp")
        try:
            with os.fdopen(handle, "w", encoding="utf-8") as file:
                json.dump([message_to_dict(message) for message in messages], file, ensure_ascii=False, indent=2)
            os.replace(temp_name, self.file_path)
        finally:
            if os.path.exists(temp_name):
                os.unlink(temp_name)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        self._write([*self.messages, *messages])

    def clear(self) -> None:
        self._write([])


def main() -> None:
    from langchain_core.messages import AIMessage, HumanMessage

    with tempfile.TemporaryDirectory() as directory:
        first = FileChatMessageHistory("lesson-demo", directory)
        first.add_messages([HumanMessage(content="Hello"), AIMessage(content="Hi!")])
        reopened = FileChatMessageHistory("lesson-demo", directory)
        print([message.content for message in reopened.messages])
        assert [message.content for message in reopened.messages] == ["Hello", "Hi!"]
        reopened.clear()
        assert reopened.messages == []


if __name__ == "__main__":
    main()
