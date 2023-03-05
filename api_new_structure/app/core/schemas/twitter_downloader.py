from pydantic import BaseModel, constr

from app.core.schemas.base import BaseResponse
from app.v1.constants import RegexPatterns


class TwitterVideoDownloaderSchema(BaseModel):
    """ TODO: add docstring """
    
    url: constr(regex=RegexPatterns.TWITTER_URL_REGEX)


class TwitterVideoDownloaderResponse(BaseResponse):
    """ TODO: add docstring """

    pass
