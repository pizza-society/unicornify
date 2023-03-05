from pydantic import EmailStr

from app.core.schemas.base import BaseResponse
from app.core.schemas.camel_case import CamelModel


class DisposableEmailSchema(CamelModel):
    """ TODO: add docstring """

    email: EmailStr


class DisposableEmailResponse(BaseResponse):
    """ TODO: add docstring """

    pass
