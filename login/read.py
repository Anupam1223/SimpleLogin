from login.schema import UserCreate, login
from sqlalchemy.orm import Session
from . import models


def create_user(db: Session, login: UserCreate):

    db_user = models.Login(
        logid=login.logid, username=login.username, password=login.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user):
    return db.query(models.Login).filter(models.Login.username == user).first()
