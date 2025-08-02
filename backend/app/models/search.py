from datetime import datetime, timezone
from sqlmodel import DateTime, SQLModel, Field, Column
import enum


# class SearchStatus(enum.Enum):
#     pending = 'pending'
#     in_progress = 'in_progress'
#     completed = 'completed'
#     failed = 'failed'

# class Search(SQLModel, table=True):
#     __tablename__ = "searches"
    
#     id: int | None = Field(default=None, primary_key=True)
#     line: str = Field(index=True, nullable=False)
#     status: SearchStatus = Field(default=SearchStatus.pending, nullable=False)
#     tag_id: int = Field(default=0, nullable=False)
#     product_ids: list[int] = Field(default=[], nullable=False)
#     created_at: DateTime = Field(default=datetime.now(), nullable=False)
#     updated_at: DateTime = Field(default=datetime.now(), sa_column=Column(DateTime, onupdate=datetime.now(timezone.utc)))
    
class SearchCreate(SQLModel):
    line: str
    tag_id: int
