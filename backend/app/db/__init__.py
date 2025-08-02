from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import all models to register them with Base for Alembic migrations
from backend.models.search import Search

