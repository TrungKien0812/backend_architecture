students = {
    1: {"name": "kien", "age": 20, "username": "kien.nguyenlovefamily", "year": "C22-KHM2"},
    2: {"name": "an", "age": 20, "username": "an.builovefamily", "year": "C23-KHM2"}
}

def get_student(student_id: int):
    return students.get(student_id)

def create_student(student_id: int, data: dict):
    students[student_id] = data
    return data

def update_student(student_id: int, data: dict):
    students[student_id].update(data)
    return students[student_id]

def delete_student(student_id: int):
    return students.pop(student_id, None)
