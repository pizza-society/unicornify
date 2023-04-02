from pydantic import BaseModel


class BaseResponse(BaseModel):
    """ Base response """

    result: str
