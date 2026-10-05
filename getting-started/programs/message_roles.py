"""Inspect LangChain message objects without an API call."""
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful Python teacher."),
    HumanMessage(content="Explain loops in one sentence."),
    AIMessage(content="A loop repeats a block of code."),
]
for message in messages:
    print(f"{type(message).__name__}: {message.content}")
