from fastapi import FastAPI

# from routes import api_router


# Create FastAPI instance
app = FastAPI()

# Register API routes
# app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok"}