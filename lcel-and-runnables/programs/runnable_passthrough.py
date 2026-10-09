"""Keep an input alongside a transformed version (September 22 lesson)."""

from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough


def main() -> None:
    branches = RunnableParallel(
        original=RunnablePassthrough(),
        doubled=RunnableLambda(lambda number: number * 2),
    )
    print(branches.invoke(10))  # {'original': 10, 'doubled': 20}


if __name__ == "__main__":
    main()
