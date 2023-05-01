import logging

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.core.docs import twitter_video_doc
from app.modules.twitter_downloader_mod import TwitterVideoDownloader
from app.core.schemas.exceptions import TweetExtractionError
from app.core.schemas.twitter_downloader import TwitterVideoDownloaderSchema, TwitterVideoDownloaderResponse


router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/download-tweet-video/",
             response_model=TwitterVideoDownloaderResponse,
             summary=twitter_video_doc.SUMMARY,
             responses=twitter_video_doc.RESPONSES,
             status_code=status.HTTP_200_OK)
def download_tweet_media(data: TwitterVideoDownloaderSchema):
    """\f
    Generate a Tweet video downloader object

    Args:

        data (TwitterVideoDownloaderSchema): A valid URL for a Twitter status, e.g. https://twitter.com/user/status/media_id

    Returns:
    
        TwitterVideoDownloaderResponse: The generated Tweet video downloader object, containing video metadata and download URL, or

        JSONResponse: Error response containing error message and status code
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
    return TwitterVideoDownloaderResponse(result=tw_data)