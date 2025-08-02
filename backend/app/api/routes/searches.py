from fastapi import APIRouter

from models.search import SearchCreate

router = APIRouter(prefix="/searches", tags=["searches"])


@router.get("/{id}")
def get_searches(id: int):
  return {"status": "test response"}

@router.post("/")
def create_search(search: SearchCreate):
  return {"status": f"test response on search request {search}"}