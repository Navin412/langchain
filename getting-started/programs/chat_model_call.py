"""Make one live model call and inspect the AIMessage."""
import os
from langchain_openai import ChatOpenAI

if not os.getenv("OPENAI_API_KEY"):
    raise SystemExit("Set OPENAI_API_KEY before running this program.")

model = ChatOpenAI(model="gpt-4o-mini")
response = model.invoke("Explain LangChain in one simple sentence.")
print("Object type:", type(response).__name__)
print("Text:", response.content)
print("Usage:", response.usage_metadata)
