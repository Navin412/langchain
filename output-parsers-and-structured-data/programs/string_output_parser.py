"""Parse an AIMessage into text without calling a model."""
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser

message = AIMessage(content="A parser converts model output for the next component.")
text = StrOutputParser().invoke(message)
print(type(text).__name__, text)
