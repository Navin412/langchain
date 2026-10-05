"""Generate restaurant names with a reusable chat prompt."""
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

if not os.getenv("OPENAI_API_KEY"):
    raise SystemExit("Set OPENAI_API_KEY before running this program.")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You suggest memorable restaurant names. Return a numbered list only."),
    ("human", "Suggest five names for a {style} {cuisine} restaurant in {location}."),
])
model = ChatOpenAI(model="gpt-4o-mini")
values = {
    "style": input("Style [casual]: ").strip() or "casual",
    "cuisine": input("Cuisine [Indian]: ").strip() or "Indian",
    "location": input("Location [Hyderabad]: ").strip() or "Hyderabad",
}
response = (prompt | model).invoke(values)
print(response.content)
