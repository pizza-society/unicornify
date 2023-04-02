import logging
from datetime import date, datetime, timedelta

import youtube_dl
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import HttpUrl

from app.core.schemas.exceptions import TweetExtractionError
from app.core.schemas.twitter_downloader import TwitterVideoDownloaderSchema, TwitterVideoDownloaderResponse


router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/download-tweet-video/",
             response_model=TwitterVideoDownloaderResponse,
             summary="Download Twitter status video")
def download_tweet_media(data: TwitterVideoDownloaderSchema):
    """
    Generate a Tweet video downloader object by using 3rd party script with all the information:

    - **url**: a valid http / https URL for twitter status 
                i.e: https://twitter.com/user/status/media_id

    Documentation about the external CLI can be found here https://github.com/ytdl-org/youtube-dl
    """

    twt_downloader_instance = TwitterVideoDownloader(data.url)

    # Call script
    try:
        tw_data = twt_downloader_instance.extract_tweet_status_info()
    except (TweetExtractionError, KeyError) as e:
        # Return a JSONResponse with an error message if there is a problem extracting the Twitter info
        error_msg = {"error": "There was an error while extracting the status: {}".format(str(e))}
        logger.error(error_msg)

        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={ "error": str(error_msg) })

    # Return response
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={ "result": tw_data })


class TwitterVideoDownloader:
    """
    TwitterVideoDownloader is a class for downloading Twitter status media.

    Attributes:
        - __ydl_opts (dict): Options for the YoutubeDL object.
        - url (HttpUrl): Link for the Twitter video

    Public Methods:
        extract_tweet_status_info() -> dict:
            Given a valid Twitter status URL, return a media object containing tweet information.
    """

    def __init__(self, url) -> None:
        """
        Initializes the `TwitterVideoDownloader` class.

        Args:
            url (HttpUrl): The URL of the Twitter video.

        """
        self.url: HttpUrl = url # Video URL

        self._ydl_options = {"outtmpl": "%(id)s.%(ext)s"}
        self._size_sample = (
            "N/A"  # To be updated, as there is no clear method to find accurate video size.
        )


    def _extract_resolution_and_link_info(self, dict_formats) -> dict:
        """
        Extract resolution and direct download link from YTDL response['format'].

        Args:
            dict_formats (dict): Dictionary of formats from the YoutubeDL response.

        Returns:
            dict: Dictionary of resolution and direct download link information.
        """
        m3u8_header = "hls-"  # hls- xxx header indicates a video with m3u8 format
        result = []
        for f in dict_formats:
            if m3u8_header not in f["format_id"]:
                info = {}
                info["format"] = f["format"]
                info["width"] = f["width"]
                info["height"] = f["height"]
                info["resolution"] = f"{f['height']} x {f['width']}"
                info["url"] = f["url"]
                info["size"] = self._size_sample
                result.append(info)

        return result

    def _extract_tweet_meta_data(self, tweet_meta_data, tweet_url) -> dict:
        """
        Extract specified data from YoutubeDL response tweet data.

        Args:
            tweet_meta_data (dict): Tweet metadata from the YoutubeDL response.
            tweet_url (str): URL of the tweet.

        Returns:
            dict: Dictionary of tweet metadata.
        """
        return {
            "tweet_url": tweet_url,
            "uploader_user_id": tweet_meta_data["uploader_id"],
            "uploader_display_name": tweet_meta_data["uploader"],
            "upload_date": self._format_date(tweet_meta_data["upload_date"]),
            "duration": self._convert_seconds_to_minutes(tweet_meta_data["duration"]),
            "thumbnail": tweet_meta_data["thumbnail"],
            "title": tweet_meta_data["title"],
            "description": tweet_meta_data["description"],
        }

    def _format_date(self, date) -> date:
        """
        Return date in yyyy-mm-dd format, given date in yyyymmddd.

        Args:
            date (str): Date in yyyymmddd format.

        Returns:
            str: Date in yyyy-mm-dd format.
        """
        return datetime.strptime(date, "%Y%m%d").strftime("%d-%m-%Y")

    def _convert_seconds_to_minutes(self, time_in_secs) -> str:
        """
        Return time in minutes without microseconds, given in seconds.

        Args:
            time_in_secs (int): Time in seconds.

        Returns:
            str: Time in minutes without microseconds.
        """
        return str(timedelta(seconds=time_in_secs)).split(".")[0]

    def extract_tweet_status_info(self) -> dict:
        """
        Given a valid Twitter status URL, return a media object containing tweet information.

        Returns:
            dict: Dictionary containing tweet information, including tweet metadata and tweet media information.
        """
        tweet_url = self.url

        try:
            with youtube_dl.YoutubeDL(self._ydl_options) as ydl:
                tweet_info_data = ydl.extract_info(tweet_url, download=False)
                tweet_media_formats = tweet_info_data.get("formats", [tweet_info_data])
        except youtube_dl.DownloadError as e:
            raise TweetExtractionError("Unable to extract tweet information") from e

        metadata = self._extract_tweet_meta_data(tweet_info_data, tweet_url)
        media = self._extract_resolution_and_link_info(tweet_media_formats)

        return {
            "tweet_meta_data": metadata,
            "tweet_medias": media,
        }
