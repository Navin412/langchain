"""Round-trip LangChain messages through dictionaries and JSON (October 6)."""

import json

from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    message_to_dict,
    messages_from_dict,
)


def main() -> None:
    messages = [
        HumanMessage(content="My name is Durga."),
        AIMessage(content="Nice to meet you, Durga."),
    ]
    dictionaries = [message_to_dict(message) for message in messages]
    json_text = json.dumps(dictionaries, ensure_ascii=False, indent=2)
    restored = messages_from_dict(json.loads(json_text))

    print("JSON text:\n", json_text)
    print("Restored messages:")
    for message in restored:
        print(type(message).__name__, ":", message.content)
    assert [type(message) for message in restored] == [HumanMessage, AIMessage]
    assert [message.content for message in restored] == [message.content for message in messages]


if __name__ == "__main__":
    main()
