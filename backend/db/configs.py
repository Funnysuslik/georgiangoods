from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, SQLModel, Session

db_url = 'postgresql+asyncpg://postgres:postgres@localhost:5432/postgres'
connect_args = {"check_same_thread": False}

engine = create_engine(db_url, echo=True, connect_args=connect_args)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]