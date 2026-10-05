"""Extract a Student object from free text using a live model call."""
import os
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class Student(BaseModel):
    name: str = Field(description="Name stated in the text")
    age: int | None = Field(default=None, description="Age if explicitly stated")
    course: str | None = Field(default=None, description="Course if explicitly stated")

if not os.getenv("OPENAI_API_KEY"):
    raise SystemExit("Set OPENAI_API_KEY before running this program.")

model = ChatOpenAI(model="gpt-4o-mini")
extractor = model.with_structured_output(Student)
student = extractor.invoke("Ravi is 22 years old and is learning Python.")
print(student.model_dump())
