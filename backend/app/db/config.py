from sqlmodel import SQLModel, create_engine

# db_url = 'postgresql+asyncpg://postgres:postgres@localhost:5432/postgres'
# connect_args = {"check_same_thread": False}

engine = create_engine(db_url, echo=True, connect_args=connect_args)

def init_db():
    SQLModel.metadata.create_all(engine)
