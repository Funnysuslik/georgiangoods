from fastapi import APIRouter

from api.routes import searches
from core.config import settings

api_router = APIRouter()
api_router.include_router(searches.router)
