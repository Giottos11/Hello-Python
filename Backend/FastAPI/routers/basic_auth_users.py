from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": False,
        "password": "123456"
    },
    "Giottos33": {
            "username": "Giottos33",
            "full_name": "José Juan",
            "email": "giottos330@gmail.com",
            "disabled": False,
            "password": "9384738"
        },
    "aitor.ct": {
                "username": "aitor.ct",
                "full_name": "Aitor Infantes",
                "email": "aitor.ct@gmail.com",
                "disabled": False,
                "password": "374838"
            },
}

def search_user(username: str):
    if username in users_db:
        return UserDB(users_db[username])