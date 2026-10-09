"""Classes 34–36: inspect the older buffer and window memory APIs.

Optional historical example: install a compatible `langchain-classic` environment
separately from the pinned modern examples in this repository.
"""

try:
    from langchain_classic.memory import ConversationBufferMemory, ConversationBufferWindowMemory
except ImportError as error:
    raise SystemExit("Install langchain-classic in a separate environment for this legacy lesson.") from error


def add_turn(memory, question: str, answer: str) -> None:
    memory.save_context({"input": question}, {"output": answer})


def main() -> None:
    full = ConversationBufferMemory(return_messages=True)
    window = ConversationBufferWindowMemory(k=2, return_messages=True)
    turns = [
        ("My name is Durga.", "Nice to meet you."),
        ("I teach Python.", "Great."),
        ("I live in Hyderabad.", "Okay."),
    ]
    for question, answer in turns:
        add_turn(full, question, answer)
        add_turn(window, question, answer)

    print("Full history:")
    for message in full.load_memory_variables({})["history"]:
        print(type(message).__name__, message.content)
    print("\nRecent two turns:")
    for message in window.load_memory_variables({})["history"]:
        print(type(message).__name__, message.content)
    full.clear()
    print("\nAfter clear:", full.load_memory_variables({}))


if __name__ == "__main__":
    main()
