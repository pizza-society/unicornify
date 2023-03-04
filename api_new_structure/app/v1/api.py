from fastapi import APIRouter

from app.v1.endpoints import qr_code as qr_code_endpoints

api_router = APIRouter()

api_router.include_router(qr_code_endpoints.router,
                          prefix='/services',
                          tags=['Services'])
