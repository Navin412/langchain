"""Offline demonstration of separate, persistent conversation histories."""

import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory


def history_path(root: Path, conversation_id: str) -> Path:
    # Transform the ID so it cannot act as a relative file path.
    digest = hashlib.sha256(conversation_id.encode("utf-8")).hexdigest()
    return root / f"{digest}.json"


def add_turn(root: Path, conversation_id: str, question: str, answer: str) -> None:
    path = history_path(root, conversation_id)
    turns = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    turns.append({"question": question, "answer": answer})
    path.write_text(json.dumps(turns, indent=2), encoding="utf-8")


def load_turns(root: Path, conversation_id: str) -> list[dict[str, str]]:
    path = history_path(root, conversation_id)
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else []


if __name__ == "__main__":
    with TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        add_turn(root, "alice-chat-1", "Favorite language?", "Python")
        add_turn(root, "bob-chat-1", "Favorite language?", "Java")
        print("Alice:", load_turns(root, "alice-chat-1"))
        print("Bob:", load_turns(root, "bob-chat-1"))
        assert len(list(root.glob("*.json"))) == 2
