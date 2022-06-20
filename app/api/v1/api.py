from fastapi import APIRouter

from app.services.api import v1 as services

api_router = APIRouter()

api_router.include_router(
    services.router,
    prefix='/services',
    tags=['Services']
)
