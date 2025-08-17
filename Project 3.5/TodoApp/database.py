from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQltie
# SQLALCHEMY_DATABASE_URL = 'sqlite:///todosapp.db'
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password123@127.0.0.1:5444/todoapp"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
