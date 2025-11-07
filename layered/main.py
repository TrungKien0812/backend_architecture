from fastapi import FastAPI
from controllers import student_controller

app = FastAPI(title="Layered Architecture Demo")
app.include_router(student_controller.router)
