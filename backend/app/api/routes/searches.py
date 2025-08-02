from fastapi import APIRouter, HTTPException

from models.search import Search, SearchCreate, SearchPublic
from app.api.deps import SessionDep

router = APIRouter(prefix="/searches", tags=["searches"])


@router.get("/{id}", response_model=SearchPublic)
def get_searches(session: SessionDep, id: int):

  item = session.get(Search, id)
  if not item:
      raise HTTPException(status_code=404, detail="Item not found")

  return {"status": "test response"}

@router.post("/")
def create_search(search: SearchCreate):
  return {"status": f"test response on search request {search}"}