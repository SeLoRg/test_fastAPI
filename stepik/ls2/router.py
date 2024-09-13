from fastapi import APIRouter
from stepik.ls2.models import Feedback


router = APIRouter()
fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}

fake_feedback = [

]


@router.get("/users/")
def get_users(limit: int):
    return dict(list(fake_users.items())[:limit])


@router.post("/feedback")
def post_feedback(feed: Feedback):
    fake_feedback.append(feed)
    return {"message": "Feedback received. Thank you, Alice!"}
