"""Choose the first matching runnable (September 24 lesson)."""

from langchain_core.runnables import RunnableBranch, RunnableLambda


def grade(marks: int) -> str:
    route = RunnableBranch(
        (lambda value: value >= 75, RunnableLambda(lambda _: "Distinction")),
        (lambda value: value >= 60, RunnableLambda(lambda _: "First Class")),
        (lambda value: value >= 35, RunnableLambda(lambda _: "Pass")),
        RunnableLambda(lambda _: "Fail"),
    )
    return route.invoke(marks)


def main() -> None:
    for marks in (85, 65, 45, 20):
        print(f"{marks}: {grade(marks)}")

    student_route = RunnableBranch(
        (
            lambda student: student["marks"] >= 35,
            RunnableLambda(lambda student: f'{student["name"]} passed the exam'),
        ),
        RunnableLambda(lambda student: f'{student["name"]} failed the exam'),
    )
    print(student_route.invoke({"name": "Ramesh", "marks": 70}))


if __name__ == "__main__":
    main()
