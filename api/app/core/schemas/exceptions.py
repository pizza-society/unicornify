class BaseException(Exception):
    DEFAULT_MESSAGE = "Error occurred"

    def __init__(self, message: str = DEFAULT_MESSAGE) -> None:
        self.message = message
        super().__init__(self.message)


class UnsupportedFormat(BaseException):
    """
    Exception raised when a supported media format could
    not be found in the video link.

    Attributes:
        message (str): The error message indicating that a
                       supported format could not be found.
    """
    DEFAULT_MESSAGE = "Unable to find a supported media format (GIF or video) in the link"
        

class UnableToFindSupportedFormatKeys(BaseException):
    """
    TODO: change this exception name to a shorter name
    Exception raised when supported media format keys could
    not be found in the dictionary returned by youtube_dl.

    Attributes:
        message (str): The error message indicating that the
                       supported format keys could not be found
                       in the dictionary returned by youtube_dl.
    """
    DEFAULT_MESSAGE = "Unable to find supported format keys in the dictionary returned by youtube_dl"


class TweetExtractionError(BaseException):
    """
    Exception raised when an error occurs during the extraction
    of data from a tweet.

    Attributes:
        message (str): The error message indicating that data could
                       not be extracted from the tweet.
    """
    DEFAULT_MESSAGE = "Unable to extract data from tweet"

