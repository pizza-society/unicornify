from typing import List

from pydantic import BaseModel, constr

from app.v1.constants import RegexPatterns
from app.core.schemas.camel_case import CamelModel


class TwitterVideoDownloaderSchema(BaseModel):
    """
    Represents the schema for a Twitter video downloader request.

    Attributes:
        url (constr): The Twitter video downloader URL.
    """

    url: constr(regex=RegexPatterns.TWITTER_URL_REGEX)


class TweetMedias(CamelModel):
    """
    Represents a media object in a tweet.

    Attributes:
        format (str): The format of the media.
        width (int): The width of the media.
        height (int): The height of the media.
        resolution (str): The resolution of the media.
        url (str): The URL of the media.
        size (str): The size of the media.
    """

    format: str
    width: int
    height: int
    resolution: str
    url: str
    size: str


class TweetMetaData(CamelModel):
    """
    Represents metadata for a tweet.

    Attributes:
        tweet_url (str): The URL of the tweet.
        uploader_user_id (str): The user ID of the uploader of the tweet.
        uploader_display_name (str): The display name of the uploader of the tweet.
        upload_date (str): The date when the tweet was uploaded.
        duration (str): The duration of the tweet.
        thumbnail (str): The URL of the thumbnail of the tweet.
        title (str): The title of the tweet.
        description (str): The description of the tweet.
    """

    tweet_url: str
    uploader_user_id: str
    uploader_display_name: str
    upload_date: str
    duration: str
    thumbnail: str
    title: str
    description: str


class TwitterVideoDownloaderResult(CamelModel):
    """
    Represents the result of a Twitter video downloader.

    Attributes:
        tweet_meta_data (TweetMetaData): The metadata of the tweet.
        tweet_medias (List[TweetMedias]): The list of media objects in the tweet.
    """

    tweet_meta_data: TweetMetaData
    tweet_medias: List[TweetMedias] = []


class TwitterVideoDownloaderResponse(CamelModel):
    """
    A response model for the Twitter video downloader.
    
    Attributes:
        result (TwitterVideoDownloaderResult): The result of the video downloader.
    """

    result: TwitterVideoDownloaderResult
