from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sql_connect = "mysql://root:@localhost/login"

engine = create_engine(sql_connect)
sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()
