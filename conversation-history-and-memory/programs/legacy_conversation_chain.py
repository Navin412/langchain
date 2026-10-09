"""Class 35: historical ConversationChain memory example.

Run in a separate environment with langchain-classic and a supported chat-model
integration. This API is preserved to help read older tutorials.
"""

import os

try:
    from langchain_classic.chains import ConversationChain
    from langchain_classic.memory import ConversationBufferWindowMemory
except ImportError as error:
    raise SystemExit("Install langchain-classic separately for this legacy example.") from error

from langchain_openai import ChatOpenAI


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this live example.")
    memory = ConversationBufferWindowMemory(k=2)
    chat = ConversationChain(llm=ChatOpenAI(model="gpt-4o-mini"), memory=memory)
    print("Historical two-turn window. Type exit to stop.")
    while True:
        question = input("You: ").strip()
        if question.lower() == "exit":
            break
        if question:
            print("AI:", chat.invoke({"input": question})["response"])


if __name__ == "__main__":
    main()
