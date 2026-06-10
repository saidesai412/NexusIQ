import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager
from loguru import logger

from app.config import settings
from app.database import init_db, close_db
from app.routers import forecast, churn, demand, risk, rag, agents


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown lifecycle."""
    logger.info(f"Starting {settings.APP_NAME}...")
    await init_db()
    logger.info("Database connections initialized")
    yield
    logger.info("Shutting down...")
    await close_db()
    logger.info("Database connections closed")


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="NexusIQ AI/ML Service — Forecasting, Churn, Demand, Risk, RAG, and Multi-Agent Intelligence",
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000", "http://localhost:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(forecast.router, prefix="/forecast", tags=["Forecast"])
app.include_router(churn.router, prefix="/churn", tags=["Churn"])
app.include_router(demand.router, prefix="/demand", tags=["Demand"])
app.include_router(risk.router, prefix="/risk", tags=["Risk"])
app.include_router(rag.router, prefix="/rag", tags=["RAG"])
app.include_router(agents.router, prefix="/agents", tags=["Agents"])


@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "version": "1.0.0",
        "environment": settings.APP_ENV,
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info",
    )
