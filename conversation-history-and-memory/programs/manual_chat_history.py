"""Terminal chatbot that stores both user and model messages in memory."""
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

if not os.getenv("OPENAI_API_KEY"):
    raise SystemExit("Set OPENAI_API_KEY before running this program.")

model = ChatOpenAI(model="gpt-4o-mini")
messages = [SystemMessage(content="You are a concise, helpful tutor.")]
print("Type 'exit' to stop. History is lost when this program closes.")
while True:
    user_text = input("You: ").strip()
    if user_text.lower() == "exit":
        break
    if not user_text:
        continue
    messages.append(HumanMessage(content=user_text))
    try:
        response = model.invoke(messages)
    except Exception:
        messages.pop()  # Keep the history consistent if this call fails.
        raise
    messages.append(response)
    print("AI:", response.content)
