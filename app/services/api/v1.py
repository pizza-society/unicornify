from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

import io
import base64
import json
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

from app.services.models import (
    DrawerChoices,
    QRCodeModel,
    QRCodeResponse,
    ShortedModel,
    ShortedResponse
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
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Return response
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            'result': img_base64
        }
    )

@router.post(
    '/generate-short-url/',
    response_model=ShortedResponse,
    summary='Generate short URL'
)
def generate_short_url(data: ShortedModel):
    """
        Generate a short URL by using 3rd party API with all the information:

        - **url**: a valid http / https URL

        Documentation about the external API can be found here https://cleanuri.com/docs
    """
    BASE_URL = 'https://cleanuri.com/api/v1/shorten'
    
    # Make request
    shorted_service = requests.post(
        BASE_URL,
        {
            'url': data.url
        }
    )

    # Catching error
    try:
        shorted_service.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Convert byte to dict / json
        error_response = json.loads(e.response.text)
        raise HTTPException(
            shorted_service.status_code,
            detail=error_response['error']
        )

    # Return service in json
    return json.loads(
        shorted_service.text
    )