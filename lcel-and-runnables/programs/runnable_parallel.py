"""Run independent branches over the same input."""
from langchain_core.runnables import RunnableLambda, RunnableParallel

branches = RunnableParallel(
    uppercase=RunnableLambda(lambda text: text.upper()),
    word_count=RunnableLambda(lambda text: len(text.split())),
    preview=RunnableLambda(lambda text: text[:12]),
)
print(branches.invoke("LangChain connects useful components"))
