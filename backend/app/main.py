from fastapi import FastAPI

from api.common import api_router
from core.config import settings


app = FastAPI()

# Register API routes
# app.include_router(api_router, prefix="/api/v1")

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/health")
def health():
    return {"status": "ok"}
