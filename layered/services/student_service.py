from repositories import student_repository

def get_student(student_id: int):
    return student_repository.get_student(student_id)

def create_student(student_id: int, data: dict):
    if student_repository.get_student(student_id):
        return {"error": "Student exists"}
    return student_repository.create_student(student_id, data)
