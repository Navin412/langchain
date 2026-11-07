"""Classes 30–33: offline exercises for stateless calls and message windows.

The PDFs use a live LLM to demonstrate these ideas. Here a deterministic
responder lets you inspect the message lists without an API key.
Run: python practice/class30_33_history.py
"""

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage


def mock_model(messages: list[BaseMessage]) -> AIMessage:
    """Echo the previous user turn if it was supplied; this is not an LLM."""
    questions = [message.content for message in messages if isinstance(message, HumanMessage)]
    context = questions[-2] if len(questions) > 1 else "no earlier user turn"
    return AIMessage(content=f"Current={questions[-1]!r}; context={context!r}")


def class30_stateless_vs_manual() -> tuple[str, str]:
    first = HumanMessage(content="My favorite language is Python")
    follow_up = HumanMessage(content="What is my favorite language?")
    stateless = mock_model([follow_up]).content
    manual = mock_model([first, AIMessage(content="I will remember that."), follow_up]).content
    assert "no earlier" in stateless and "Python" in manual
    return stateless, manual


def class31_dynamic_history(turns: list[str]) -> list[BaseMessage]:
    history: list[BaseMessage] = []
    for question in turns:
        history.append(HumanMessage(content=question))
        history.append(mock_model(history))
    return history


def class32_recent_window(history: list[BaseMessage], turns: int) -> list[BaseMessage]:
    """Each turn has a HumanMessage and an AIMessage."""
    return history[-2 * turns :] if turns > 0 else []


def class33_system_and_recent(history: list[BaseMessage], turns: int) -> list[BaseMessage]:
    return [SystemMessage(content="You are a concise Python tutor."), *class32_recent_window(history, turns)]


if __name__ == "__main__":
    print("Class 30:", class30_stateless_vs_manual())
    history = class31_dynamic_history(["I live in Boston", "I study Python", "What do I study?"])
    recent = class32_recent_window(history, turns=2)
    sent = class33_system_and_recent(history, turns=2)
    assert len(history) == 6 and len(recent) == 4 and len(sent) == 5
    print("Class 31 stored messages:", len(history))
    print("Class 32 recent messages:", [message.content for message in recent])
    print("Class 33 sent types:", [type(message).__name__ for message in sent])
