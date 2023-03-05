from fastapi import APIRouter

from app.v1 import constants
from app.v1.endpoints import disposable_email as disposable_email_endpoints
from app.v1.endpoints import qr_code as qr_code_endpoints
from app.v1.endpoints import reverse_proxy as reverse_proxy_endpoints
from app.v1.endpoints import tiktok_downloader as tiktok_downloader_endpoints
from app.v1.endpoints import twitter_downloader as twitter_downloader_endpoints


api_router = APIRouter()
api_router.include_router(disposable_email_endpoints.router,
                          prefix=constants.SERVICES_ENDPOINT,
                          tags=[constants.SERVICES_TAG])
api_router.include_router(qr_code_endpoints.router,
                          prefix=constants.SERVICES_ENDPOINT,
                          tags=[constants.SERVICES_TAG])
api_router.include_router(reverse_proxy_endpoints.router,
                          prefix=constants.SERVICES_ENDPOINT,
                          tags=[constants.SERVICES_TAG])
api_router.include_router(tiktok_downloader_endpoints.router,
                          prefix=constants.SERVICES_ENDPOINT,
                          tags=[constants.SERVICES_TAG])
api_router.include_router(twitter_downloader_endpoints.router,
                          prefix=constants.SERVICES_ENDPOINT,
                          tags=[constants.SERVICES_TAG])
