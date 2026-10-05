"""A small learning assistant adapted from the supplied workshop."""
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

if not os.getenv("OPENAI_API_KEY"):
    raise SystemExit("Set OPENAI_API_KEY before running this program.")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a patient learning assistant. Be accurate and approachable."),
    ("human", "Teach {topic} to a {level} learner. Give a simple explanation, "
              "five important points, and one practical example."),
])
chain = prompt | ChatOpenAI(model="gpt-4o-mini") | StrOutputParser()
topic = input("Topic [LangChain]: ").strip() or "LangChain"
level = input("Level [beginner]: ").strip() or "beginner"
print(chain.invoke({"topic": topic, "level": level}))
