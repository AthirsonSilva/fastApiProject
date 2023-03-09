from typing import List, Dict
from uuid import uuid4, UUID

from fastapi import FastAPI

from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("56a6250f-eabb-4c46-875f-8f3298ae7bf6"),
        first_name="John",
        last_name="Doe",
        middle_name="Smith",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
    User(
        id=UUID("da4726ca-164e-406c-af39-da5e53244f81"),
        first_name="Mary",
        last_name="Doe",
        middle_name="Smith",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=UUID("5cb37849-0c8d-40b4-99a9-ddc3ca184600"),
        first_name="Gregory",
        last_name="Doe",
        middle_name="Rose",
        gender=Gender.male,
        roles=[Role.student],
    ),
]


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}


@app.get("/api/v1/users")
async def fetch_users() -> dict[str, str | list[User]]:
    return {"message": "Students fetched successfully!", "data": db}
