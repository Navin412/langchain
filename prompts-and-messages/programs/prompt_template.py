"""Format a reusable text prompt without calling a model."""
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template("Explain {topic} at a {level} level.")
prompt = template.invoke({"topic": "Python lists", "level": "beginner"})
print("Variables:", template.input_variables)
print(prompt.to_string())
