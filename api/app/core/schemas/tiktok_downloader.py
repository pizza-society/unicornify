from pydantic import BaseModel, constr

from app.core.schemas.base import BaseResponse
from app.v1.constants import RegexPatterns


class TikTokVideoDownloaderSchema(BaseModel):
    """ TODO: add docstring """

    url: constr(regex=RegexPatterns.TIKTOK_URL_REGEX)


class TikTokVideoDownloaderResponse(BaseResponse):
    """ TODO: add docstring """

    pass

