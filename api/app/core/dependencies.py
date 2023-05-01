from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.utils.exceptions import custom_http_exception_handler, validation_exception_handler


EXCEPTION_HANDLERS = [
    (StarletteHTTPException, custom_http_exception_handler),
    (RequestValidationError, validation_exception_handler)
]


def setup_handlers(app: FastAPI):
    """ Add custom handlers into app """
    for handler in EXCEPTION_HANDLERS:
        app.add_exception_handler(handler[0], handler[1])
