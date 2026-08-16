### Users API con autorización OAuth2 JWT ###

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


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
        "password": "$2a$12$Z/g7Uuk4U/pFImD41.oJuOWjPSgUwkUT.Q/dkSUGWAez.2kblDt/K"
    },
    "Giottos33": {
        "username": "Giottos33",
        "full_name": "José Juan",
        "email": "giottos330@gmail.com",
        "disabled": False,
        "password": "$2a$12$porlDxy38hxaU5.CpPRUpOVDJgMEA/OWmwFSQConQcXytze2VG3dW"      #"938473"
    },
    "aitor.ct": {
        "username": "aitor.ct",
        "full_name": "Aitor Infantes",
        "email": "aitor.ct@gmail.com",
        "disabled": False,
        "password": "$2a$12$4o64po3qQ3wCqsde8TSmgeGE4Q7Rabqnwr0QQAL3ukJo5.KugBtlu"      #"374838"
    },
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    access_token = {"sub": user.username,
                     "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {"access_token": access_token, "token_type": "bearer"}
