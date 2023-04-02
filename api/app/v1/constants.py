""" API related constants """
from enum import Enum


SERVICES_TAG = "Services"
SERVICES_ENDPOINT = "/services"

class Encoding(str, Enum):
    """
    Enum class for encodings
    """

    UTF8 = "utf-8"


class RegexPatterns:
    """
    A collection of regular expression patterns for commonly used URLs.

    Attributes:
        TWITTER_URL_REGEX (re.Pattern): A regular expression pattern for matching Twitter status URLs.
        TIKTOK_URL_REGEX (re.Pattern): A regular expression pattern for matching TikTok video URLs.
    """

    TWITTER_URL_REGEX = r"^https?:\/\/(?:mobile.)?twitter\.com\/(?:#!\/)?(\w+)\/status(?:es)?\/(\d+)(?:\/.*)?(\?(.+))?$"
    TIKTOK_URL_REGEX = r"\bhttps?:\/\/(?:m|www|vm)\.tiktok\.com\/(?:.*\b(?:(?:usr|v|embed|user|video)\/|\?shareId=|\&item_id=)(\d+)\b|([\w\d]+))"

