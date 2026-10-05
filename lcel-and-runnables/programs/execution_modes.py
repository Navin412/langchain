"""Compare invoke, batch, and stream on one no-network runnable."""
from langchain_core.runnables import RunnableLambda

square = RunnableLambda(lambda number: number * number)
print("invoke:", square.invoke(4))
print("batch:", square.batch([2, 3, 4]))
print("stream:", list(square.stream(5)))
