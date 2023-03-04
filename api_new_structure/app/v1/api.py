from fastapi import APIRouter

from app.v1.endpoints import qr_code as qr_code_endpoints
from app.v1 import constants

api_router = APIRouter()

api_router.include_router(qr_code_endpoints.router,
                          prefix=constants.SERVICES_ENDPOINT,
                          tags=[constants.SERVICES_TAG])
