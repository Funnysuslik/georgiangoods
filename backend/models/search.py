from sqlmodel import DateTime, SQLModel, Field
from sqlmodel.sql.expression import func
import enum


class SearchStatus(enum.Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    completed = 'completed'
    failed = 'failed'

class Search(SQLModel, table=True):
    __tablename__ = "searches"
    
    id: int | None = Field(default=None, primary_key=True)
    line: str = Field(index=True, nullable=False)
    date: DateTime = Field(default=func.now(), nullable=False)
    status: SearchStatus = Field(default=SearchStatus.pending, nullable=False)
    tag_ids: list[int] = Field(default=[], nullable=False)
    product_ids: list[int] = Field(default=[], nullable=False)
    created_at: DateTime = Field(default=func.now(), nullable=False)
    updated_at: DateTime = Field(default=func.now(), nullable=False, onupdate=func.now())
    
