"""Format separate system and user messages without an API call."""
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are a patient {subject} tutor. Keep answers concise."),
    ("human", "Explain {topic} for a {level} learner."),
])
prompt = template.invoke({"subject": "Python", "topic": "loops", "level": "beginner"})
for message in prompt.messages:
    print(f"{type(message).__name__}: {message.content}")
