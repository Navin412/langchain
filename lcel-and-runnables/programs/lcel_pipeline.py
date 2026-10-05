"""Compose a prompt, model, and text parser into one live chain."""
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

if not os.getenv("OPENAI_API_KEY"):
    raise SystemExit("Set OPENAI_API_KEY before running this program.")

prompt = ChatPromptTemplate.from_messages([
    ("system", "Explain concepts accurately to beginners."),
    ("human", "Explain {topic} in three sentences."),
])
chain = prompt | ChatOpenAI(model="gpt-4o-mini") | StrOutputParser()
print(chain.invoke({"topic": "Python dictionaries"}))
