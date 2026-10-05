"""Keep a system instruction plus recent conversation messages."""
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

system = SystemMessage(content="You are a helpful tutor.")
history = []
for number in range(1, 6):
    history.extend([
        HumanMessage(content=f"Question {number}"),
        AIMessage(content=f"Answer {number}"),
    ])

last_n_messages = 6
model_input = [system, *history[-last_n_messages:]]
for message in model_input:
    print(f"{type(message).__name__}: {message.content}")
