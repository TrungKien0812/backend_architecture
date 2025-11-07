from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

app = FastAPI()

class User(BaseModel):
    name: str

event_queue = asyncio.Queue()

@app.post("/register")
async def register_user(user: User):
    await event_queue.put(user.name)
    return {"message": f"User {user.name} registered!"}

async def send_welcome_emails():
    while True:
        user_name = await event_queue.get()
        print(f" Sending welcome email to {user_name}")
        event_queue.task_done()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(send_welcome_emails())
