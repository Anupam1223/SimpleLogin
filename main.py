from starlette.routing import Host
from login import models, read, schema
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from login.connection import sessionlocal, engine
from fastapi.encoders import jsonable_encoder
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/add_user/", response_model=schema.User)
def add_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    return read.create_user(db, user)


@app.get("/get_user/{username}", response_model=schema.login)
def get_user(username: str, db: Session = Depends(get_db)):
    value = jsonable_encoder(
        db.query(models.Login).filter(models.Login.username == username).first()
    )
    return value


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
