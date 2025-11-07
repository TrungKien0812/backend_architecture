from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI(title="Monolithic Architecture Demo")

students = {
    1: {"name": "kien", "age": 20, "username": "kien.nguyenlovefamily", "year": "C22-KHM2"},
    2: {"name": "an", "age": 20, "username": "an.builovefamily", "year": "C23-KHM2"}
}

class Student(BaseModel):
    name: str
    age: int
    username: str
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    username: Optional[str] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return {"message": "Monolithic Architecture Running!"}

@app.get("/students/{student_id}")
def get_student(student_id: int = Path(..., gt=0, lt=10)):
    return students.get(student_id, {"error": "Not Found"})

@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "Student already exists"}
    students[student_id] = student.dict()
    return students[student_id]

@app.put("/students/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "Not Found"}
    for key, value in student.dict(exclude_none=True).items():
        students[student_id][key] = value
    return students[student_id]

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Not Found"}
    del students[student_id]
    return {"message": "Deleted successfully"}
