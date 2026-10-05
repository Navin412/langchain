"""Validate and export structured data without calling a model."""
from pydantic import BaseModel, Field, ValidationError

class Student(BaseModel):
    name: str = Field(description="Student's name")
    age: int | None = Field(default=None, description="Age if stated")
    course: str = Field(description="Course name")

student = Student(name="Ravi", age=22, course="Python")
print(student.model_dump())
print(student.model_dump_json())
try:
    Student(name="Ravi", age="unknown", course="Python")
except ValidationError as error:
    print("Validation rejected an invalid age:", error.errors()[0]["msg"])
