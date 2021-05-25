from pydantic import BaseModel


class User(BaseModel):
    logid: int
    username: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    logid: int
    username: str
    password: str


class login(BaseModel):
    username: str
