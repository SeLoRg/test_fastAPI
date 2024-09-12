from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "trader", "name": "Alex"},
    {"id": 3, "role": "investor", "name": "Max"},
    {"id": 4, "role": "proger", "name": "Ros", "degree": [
        {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
    ]}
]


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: str


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = None


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


fake_tades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12}
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)  # Максимальная длина строки
    side: str
    price: float
    amount: float = Field(ge=0)


@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_tades.extend(trades)
    return {"OK": True, "data": fake_tades}
