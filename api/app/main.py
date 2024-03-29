from functools import lru_cache

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.v1.api import api_router
from app.core import dependencies
from app.core.settings import settings
from app.utils import logger


@lru_cache()
def get_settings():
    # https://fastapi.tiangolo.com/advanced/settings/#creating-the-settings-only-once-with-lru_cache
    return settings


app = FastAPI(title=get_settings().PROJECT_NAME,
              openapi_url=f"{ get_settings().API_V1_STR }/openapi.json")

# CORS config
# https://fastapi.tiangolo.com/tutorial/cors/#use-corsmiddleware

if get_settings().BACKEND_CORS_ORIGINS:
    app.add_middleware(CORSMiddleware,
                       allow_origins=[str(origin) for origin in get_settings().BACKEND_CORS_ORIGINS],
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"])

app.include_router(api_router, prefix=get_settings().API_V1_STR)

# Start dependencies here
dependencies.setup_handlers(app=app)

# Logger
logger.setup_logger()
