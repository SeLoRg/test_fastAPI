from typing import List, Union
from fastapi import APIRouter
from stepik.models import User, ReturnUser


router = APIRouter()
fake_users = [
    {"id": 1, "name": "Bob", "age": 15},
    {"id": 2, "name": "Alex", "age": 23},
    {"id": 3, "name": "Max", "age": 17},
]


@router.get("/users", response_model=List[User])
def get_user():
    return fake_users


@router.post("/user", response_model=List[Union[User, ReturnUser]])
def add_user(users: List[User]):
    new_users = [ReturnUser(**user.model_dump(), is_adult=user.age >= 18) for user in users]
    fake_users.extend(new_users)
    return fake_users
