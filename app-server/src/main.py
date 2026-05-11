from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.config import settings
from src.database import engine, Base
from src.auth.router import router as auth_router
from src.analysis.router import router as analysis_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app_kwargs = {
    "title": settings.PROJECT_NAME,
    "version": "1.0.0",
    "lifespan": lifespan,
}

if settings.ENVIRONMENT not in settings.SHOW_DOCS_IN:
    app_kwargs["openapi_url"] = None

app = FastAPI(**app_kwargs)

@app.get("/", tags=["health"])
@app.get("/health", tags=["health"])
async def health_check():
    return {
        "status": "healthy",
        "message": f"{settings.PROJECT_NAME} server is running."
    }

# Include routers
app.include_router(auth_router, prefix=settings.API_STR)
app.include_router(analysis_router, prefix=settings.API_STR)
