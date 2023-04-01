from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.utils.logger import get_logger
from app.core.schemas.tiktok_downloader import TikTokVideoDownloaderSchema, TikTokVideoDownloaderResponse
from app.modules.tiktok_downloader_mod import TikTokVideoDownloader


router = APIRouter()
logger = get_logger(__name__)

@router.post("/download-tiktok-video/",
             response_model=TikTokVideoDownloaderResponse,
             summary="Download TikTok video")
def download_tiktok_media(data: TikTokVideoDownloaderSchema):
    """
    TODO: Update docstring format
    Generate a Tiktok video downloader object by using 3rd party script with all the information.

    - **url**: a valid http/https URL for a TikTok video, e.g. https://www.tiktok.com/@user/video/0123456789

    Documentation about the external CLI can be found here: https://github.com/ytdl-org/youtube-dl
    """
    tiktok_downloader = TikTokVideoDownloader(data.url)

    # Call script
    try:
        tiktok_info = tiktok_downloader.extract_tiktok_media_info()
    except Exception as e:
        # Return a JSONResponse with an error message if there is a problem extracting the TikTok media info
        e = {"error": "There was an error while downloading the video: {}".format(str(e))}
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={ "error": str(e) })
    
    # Return response
    return TikTokVideoDownloaderResponse(result=tiktok_info)