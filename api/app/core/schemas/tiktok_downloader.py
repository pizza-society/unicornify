from pydantic import BaseModel, constr
from typing import List

from app.core.schemas.camel_case import CamelModel
from app.v1.constants import RegexPatterns


class TikTokVideoDownloaderSchema(BaseModel):
    """ TODO: add docstring """

    url: constr(regex=RegexPatterns.TIKTOK_URL_REGEX)


class TikTokVideoMedia(CamelModel):
    """ TODO: Rabee to improve if needed """

    format_id: str
    format_note: str
    vcodec: str
    url: str
    resolution: str


class TikTokVideoDownloaderResult(CamelModel):
    """ TODO: Rabee to improve if needed """

    medias: List[TikTokVideoMedia] = []
    creator: str
    uploader: str
    title: str
    description: str
    duration_string: str
    media_type: str
    thumbnail: str
    format: str


class TikTokVideoDownloaderResponse(CamelModel):
    """ TODO: add docstring """

    result: TikTokVideoDownloaderResult