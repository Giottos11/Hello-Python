

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Inicia el server: python -m uvicorn users:app --reload

# Entidad user


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1,name="José Juan", surname="Lara", url="https://github.com/Giottos11", age="33"),
              User(id=2,name="Brais",surname="Moure",
                   url="https://moure.dev",age=35),
              User(id=3,name="Giottos",surname="Ciber",url="https://github.com/Giottos11",age=33)]


@app.get("/usersjson")
async def usersjson():
    return [{"name":"José Juan", "surname":"Lara", "url":"https://github.com/Giottos11", "age":33},
            {"name":"Brais", "surname":"Moure", 
             "url":"https://moure.dev", "age":35},
            {"name":"Giottos", "surname":"Ciber", "url":"https://github.com/Giottos11", "age":33}]


@app.get("/users")
async def users():
    return users_list


@app.get("/user/{id}") # Path
async def user(id: int):
    return search_user(id)


@app.get("/user/") # Query
async def user(id: int):
    return search_user(id)

@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
    