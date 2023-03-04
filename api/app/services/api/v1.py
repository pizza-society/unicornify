from http.client import HTTPException
import json
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

import io
import base64
import qrcode
import requests

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styles.moduledrawers import (
    SquareModuleDrawer,
    GappedSquareModuleDrawer,
    CircleModuleDrawer,
    RoundedModuleDrawer,
    VerticalBarsDrawer,
    HorizontalBarsDrawer
)
from app.services.helpers import TwitterVideoDownloader

from app.services.models import (
    DisposableEmailModel,
    DisposableEmailResponse,
    DrawerChoices,
    QRCodeModel,
    QRCodeResponse,
    TwitterVideoDownloaderModel,
    TwitterVideoDownloaderResponse,
)

router = APIRouter()

@router.post(
    '/generate-qr-code/',
    response_model=QRCodeResponse,
    summary='Generate QR code'
)
def generate_qr(data: QRCodeModel):
    """
        Generate a QR code with all the information:

        - **url**: a valid http / https URL
        - **imageType**: [png / jpeg] ; optional, default = png
        - **drawer**: [1-Square / 2-GappedSquare / 3-Circle / 4-Rounded / 5-Vertical / 6-Horizontal] ; optional, default = 1
        - **frontColor**: [name / hex / rgb@rgba tuples / rgb@rgba string / hsl string ] ; optional, default = rgb(0, 0, 0)
        - **backColor**: [name / hex / rgb@rgba tuples / rgb@rgba string / hsl string ] ; optional, default = rgb(255, 255, 255)
    """
    # Configure
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Get drawer module
    if data.drawer == DrawerChoices.GAPPEDM:
        drawer_module = GappedSquareModuleDrawer()
    elif data.drawer == DrawerChoices.CIRCLEM:
        drawer_module = CircleModuleDrawer()
    elif data.drawer == DrawerChoices.ROUNDEDM:
        drawer_module = RoundedModuleDrawer()
    elif data.drawer == DrawerChoices.VERTICALM:
        drawer_module = VerticalBarsDrawer()
    elif data.drawer == DrawerChoices.HORIZONTALM:
        drawer_module = HorizontalBarsDrawer()
    else:
        drawer_module = SquareModuleDrawer()

    # Generate
    qr.add_data(data.url)
    qr.make(fit=True)
    buffer = io.BytesIO()
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=drawer_module,
        color_mask=SolidFillColorMask(
            front_color=data.front_color.as_rgb_tuple(),
            back_color=data.back_color.as_rgb_tuple()
        )
    )

    # Saving as data type
    img.save(buffer, format=data.image_type)

    # Encode base 64 and decode utf-8
    img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    # Return response
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "result": img_base64
        }
    )

@router.post(
    '/download-tweet-video/',
    response_model=TwitterVideoDownloaderResponse,
    summary='Download Twitter status video'
)
def download_tweet_media(data: TwitterVideoDownloaderModel):
    """
        Generate a Tweet video downloader object by using 3rd party script with all the information:

        - **url**: a valid http / https URL for twitter status 
                   i.e: https://twitter.com/user/status/media_id

        Documentation about the external CLI can be found here https://github.com/ytdl-org/youtube-dl
    """
    tw_downloader = TwitterVideoDownloader()
    # Call script
    try:
        tw_data = tw_downloader.extract_tweet_status_info(tweet_url=data.url)
    except:
        tw_data = {"error": "There's no video in this tweet"}

    # Return response
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'result': tw_data
        }
    )

@router.post(
    '/validate-disposable-email/',
    response_model=DisposableEmailResponse,
    summary='Validate disposable email'
)
async def validate_disposable_email(data: DisposableEmailModel):
    """
        Validate disposable Email by using 3rd party API with all the information:

        - **email**: a valid email address

        Documentation about the external API can be found here https://www.disify.com/
    """
    BASE_URL = f'https://www.disify.com/api/email'

    # Make request
    disposable_email_service = requests.get(
        f'{BASE_URL}/{data.email}'
    )

    # Catching error
    try:
        disposable_email_service.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Convert byte to dict / json
        error_response = json.loads(e.response.text)
        raise HTTPException(
            disposable_email_service.status_code,
            detail=error_response['error']
        )
    
    # Return response
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'result': disposable_email_service.json()
        }
    )