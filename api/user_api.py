from fastapi import FastAPI, status
from pydantic import BaseModel
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

from db.models import DbUser

app = FastAPI()
user_db = DbUser()


class User(BaseModel):
    login: str
    name: str
    email: str
    status: str


class Answer(BaseModel):
    poll_id: int
    login: str
    date: str
    time: str
    answer: int = 0
    status: str = 'skipped'


@app.get("/user/exists/{login}")
def is_user_exists(login: str):
    amount = user_db.is_user_exists(login)

    if amount:
        return status.HTTP_200_OK

    return status.HTTP_404_NOT_FOUND


@app.post("/user/signup")
def add_user(user: User):
    if not user_db.is_user_exists(user.login):
        user_db.add_user(user.login, user.name, user.email, user.status)
        return status.HTTP_200_OK

    return status.HTTP_400_BAD_REQUEST


@app.post("/user/answer")
def add_answer(answer: Answer):
    user_db.add_answer(answer.poll_id, answer.login, answer.date, answer.time, answer.answer, answer.status)
    return status.HTTP_200_OK


@app.post("/user/answer/skipped")
def add_answer_skipped(answer: Answer):
    user_db.add_answer_skipped(answer.poll_id, answer.login, answer.date, answer.time)
    return status.HTTP_200_OK
