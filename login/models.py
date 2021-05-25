from .connection import Base

from sqlalchemy import Column, Integer, String


class Login(Base):
    __tablename__ = "login"

    logid = Column(Integer, primary_key=True)
    username = Column(String(20))
    password = Column(String(20))
