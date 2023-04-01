import logging
from collections import defaultdict

import yt_dlp
from pydantic import HttpUrl

from app.core.schemas.exceptions import UnsupportedFormat, UnableToFindSupportedFormatKeys
from app.core.schemas.tiktok_downloader import TikTokVideoDownloaderResult


class TikTokVideoDownloader:
    """
    TikTokVideoDownloader is a class for downloading TikTok videos.

    Attributes:
        - __ydl_opts (dict): Options for the YoutubeDL object.
        - url (HttpUrl): Link for the Tiktok video

    Public Methods:
        extract_tiktok_media_info() -> dict:
            Extract information about a Tiktok video given its URL.
    """

    def __init__(self, url) -> None:
        """
        Initializes the `TikTokVideoDownloader` class.

        Args:
            url (HttpUrl): The URL of the TikTok video.

        """
        self.url: HttpUrl = url # Video URL
        self._ydl_opts = {} # Options for the YoutubeDL object

    def _check_format(self, format: dict) -> bool:
        """
        Check if a video format is acceptable.

        Args:
            format (dict): A dictionary representing a video format.

        Returns:
            bool: True if the format is acceptable, False otherwise.
        """
        # Acceptable format values
        valid_vcode_formats = ["h264"]

        return (format.get("format_id")
                and format.get("resolution")
                and format.get("vcodec") in valid_vcode_formats
                and format.get("format_id", "").endswith("-0"))
        
    def _filter_medias_formats(self, formats_list: list) -> dict:
        """
        Filter a list of video formats to only include acceptable formats.

        Args:
            formats_list (list): A list of dictionaries representing different video formats.

        Returns:
            dict: A dictionary containing only the acceptable formats from the input list. Each entry in the dictionary contains the
                'format_id', 'format_note', 'vcodec', 'url', and 'resolution' for a given format.
        """
        filtered_formats = filter(self._check_format, formats_list)
        filtered_formats_list = []
        
        for format in filtered_formats:
            format_dict = {}
            format_dict["format_id"] = format.get("format_id")
            format_dict["format_note"] = "MP4 - Watermarked" if "watermarked" in format.get("format_note", "") else "MP4"
            format_dict["vcodec"] = format.get("vcodec")
            format_dict["url"] = format.get("url")
            format_dict["resolution"] = format.get("resolution")
            filtered_formats_list.append(format_dict)
        
        return filtered_formats_list

    def _format_selector(self, media_info: dict) -> dict:
        """
        Select and process selected pieces of information about a video.

        Args:
            media_info (dict): A dictionary containing information about a video.

        Returns:
            dict: A dictionary containing selected pieces of information about the video. Includes the 'creator', 'uploader', 'title',
                'description', 'duration_string', and 'thumbnail' for the video. Also includes a key, 'medias', that contains the
                filtered list of formats for the video as returned by the '_filter_medias_formats' function.
        """
        # Formats are already sorted worst to best
        formats = media_info.get("formats")[::-1]

        # Variables
        processed_info = defaultdict(lambda: "N/A")
        processed_info["medias"] = {}

        keys = ["creator", "uploader", "title", "description", "duration_string", "_type", "thumbnail", "format"]

        for key in keys:
            processed_info[key] = media_info.get(key, "N/A")

        # Extract medias data
        processed_info["medias"] = self._filter_medias_formats(formats)
        
        return processed_info

    def extract_tiktok_media_info(self) -> TikTokVideoDownloaderResult:
        """
        Extract information about a TikTok video given its URL.

        Args:
            URL (HttpUrl): The URL of the TikTok video.

        Returns:
            dict: A dictionary containing information about the video. Includes the 'creator', 'uploader', 'title', 'description',
                'duration_string', and 'thumbnail' for the video. Also includes a key, 'medias', that contains a filtered list of video
                formats for the video, as returned by the '_filter_medias_formats' method. The list is sorted from worst to best quality.

        Raises:
            UnsupportedFormat: If the video format is not supported.
            UnableToFindSupportedFormatKeys: If the required information about the video's formats is not found.
            RuntimeError: If any other error occurs while extracting the video information.
        """
        try:
            with yt_dlp.YoutubeDL(self._ydl_opts) as ydl:
                info = ydl.extract_info(self.url, download=False)
        except Exception as e:
            logging.error(f"Error occurred while extracting TikTok video information: {e}")
            raise UnsupportedFormat from e

        try:
            formatted_media = self._format_selector(ydl.sanitize_info(info))

            if formatted_media is None:
                raise UnableToFindSupportedFormatKeys
        except Exception as e:
            logging.error(f"Error occurred while extracting TikTok video information: {e}")
            raise RuntimeError from e
        
        # Convert _type key to media_type as _type will be removed when TikTokVideoDownloaderResult is instantiated
        # This part can be moved into _format_selector also, please review this part since this is just an idea.
        formatted_media['media_type'] = formatted_media.pop('_type')
        return TikTokVideoDownloaderResult(**formatted_media)

