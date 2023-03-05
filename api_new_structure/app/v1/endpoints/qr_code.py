import io
import base64

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styles.moduledrawers import (SquareModuleDrawer, GappedSquareModuleDrawer,
    CircleModuleDrawer, RoundedModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer)

from app.core.schemas.qr_code import DrawerChoices, QRCode, QRCodeResponse


router = APIRouter()


@router.post("/generate-qr-code/",
             response_model=QRCodeResponse,
             summary="Generate QR code")
def generate_qr(data: QRCode):
    """
    Generate a QR code

    :param data: the qr code generator settings
    :type QRCode

    TODO:
        Update this docstring
    """
    # Configure
    qr = qrcode.QRCode(version=1, box_size=10, border=4,
                       error_correction=qrcode.constants.ERROR_CORRECT_L)
    drawer_module = get_drawer_module(data.drawer)

    # Generate
    qr.add_data(data.url)
    qr.make(fit=True)
    buffer = io.BytesIO()
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=drawer_module,
                        color_mask=SolidFillColorMask(front_color=data.front_color.as_rgb_tuple(),
                                                      back_color=data.back_color.as_rgb_tuple()))

    # Saving as data type
    img.save(buffer, format=data.image_type)

    # Encode base 64 and decode utf-8
    img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    # Return response
    return JSONResponse(status_code=status.HTTP_201_CREATED,
                        content={ "result": img_base64 })


def get_drawer_module(drawer: DrawerChoices):
    """ Get drawer module by enum choice """
    match drawer:
        case DrawerChoices.GAPPEDM:
            return GappedSquareModuleDrawer()
        case DrawerChoices.CIRCLEM:
            return CircleModuleDrawer()
        case DrawerChoices.ROUNDEDM:
            return RoundedModuleDrawer()
        case DrawerChoices.VERTICALM:
            return VerticalBarsDrawer()
        case DrawerChoices.HORIZONTALM:
            return HorizontalBarsDrawer()
        case _:
            return SquareModuleDrawer()
