"""Chain dependent Python operations using LCEL."""
from langchain_core.runnables import RunnableLambda

add_ten = RunnableLambda(lambda value: value + 10)
double = RunnableLambda(lambda value: value * 2)
subtract_five = RunnableLambda(lambda value: value - 5)
chain = add_ten | double | subtract_five
print(chain.invoke(3))  # (3 + 10) * 2 - 5 = 21
