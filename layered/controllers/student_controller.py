from fastapi import APIRouter, Path
from pydantic import BaseModel
from typing import Optional
from services import student_service

router = APIRouter()

class Student(BaseModel):
    name: str
    age: int
    username: str
    year: str

@router.get("/students/{student_id}")
def get_student(student_id: int):
    return student_service.get_student(student_id)

@router.post("/students/{student_id}")
def create_student(student_id: int, student: Student):
    return student_service.create_student(student_id, student.dict())
