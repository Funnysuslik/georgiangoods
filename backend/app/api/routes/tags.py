from fastapi import APIRouter, HTTPException

from models.tags import Tag, TagPublic
from app.api.deps import SessionDep

router = APIRouter(prefix="/tags", tags=["tags"])


@router.get("/{id}", response_model=TagPublic)
def read_item(session: SessionDep, id: int) -> Any:
    """
    Get item by ID.
    """
    item = session.get(Tag, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # return item
    return {"status": "test response"}


@router.post("/")
def create_search(search: TagPublic):
  return {"status": f"test response on search request {search}"}