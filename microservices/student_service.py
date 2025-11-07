from fastapi import FastAPI

app = FastAPI(title="Student Microservice")

students = {
    1: {"name": "kien", "age": 20, "year": "C22-KHM2"},
    2: {"name": "an", "age": 20, "year": "C23-KHM2"}
}

@app.get("/students")
def get_all_students():
    return students
