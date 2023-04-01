from pydantic import BaseModel, constr
from typing import List

from app.core.schemas.camel_case import CamelModel
from app.v1.constants import RegexPatterns


class TikTokVideoDownloaderSchema(BaseModel):
    """
    Represents the schema for a TikTok video downloader request.

    Attributes:
        url (constr): The TikTok video downloader URL.
    """

    url: constr(regex=RegexPatterns.TIKTOK_URL_REGEX)


class TikTokVideoMedia(CamelModel):
    """
    Represents TikTok video media.

    Attributes:
        format_id (str): The ID of the format.
        format_note (str): The format note.
        vcodec (str): The video codec.
        url (str): The URL of the video media.
        resolution (str): The resolution of the video media.
    """

    format_id: str
    format_note: str
    vcodec: str
    url: str
    resolution: str


class TikTokVideoDownloaderResult(CamelModel):
    """
    Represents the result of the TikTok video downloader.

    Attributes:
        medias (List[TikTokVideoMedia]): The list of media for the video.
        creator (str): The creator of the video.
        uploader (str): The uploader of the video.
        title (str): The title of the video.
        description (str): The description of the video.
        duration_string (str): The duration of the video.
        media_type (str): The type of media in the video.
        thumbnail (str): The URL of the video thumbnail.
        format (str): The format of the video.
    """

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
    """
    A response model for the TikTok video downloader.

    Attributes:
        result (TikTokVideoDownloaderResult): The result of the video downloader.
    """

    result: TikTokVideoDownloaderResult
