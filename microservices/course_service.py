from fastapi import FastAPI

app = FastAPI(title="Course Microservice")

courses = {
    1: {"title": "Operating Systems", "credits": 3},
    2: {"title": "Database Systems", "credits": 4}
}

@app.get("/courses")
def get_all_courses():
    return courses
