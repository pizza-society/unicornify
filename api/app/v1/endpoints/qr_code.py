import io
import base64

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

import qrcode
from qrcode.exceptions import DataOverflowError
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles import colormasks, moduledrawers

from app.v1 import constants
from app.core.docs import qr_code_doc
from app.core.schemas.qr_code import DrawerChoices, QRCode, QRCodeResponse
from app.core.schemas.errors import ErrorCode
from app.utils.logger import get_logger as logger


VERSION = 1
BOX_SIZE = 10
BORDER = 4

router = APIRouter()


@router.post("/generate-qr-code/",
             response_model=QRCodeResponse,
             summary=qr_code_doc.SUMMARY,
             description=qr_code_doc.DESCRIPTION,
             responses=qr_code_doc.RESPONSES,
             status_code=status.HTTP_201_CREATED)
def generate_qr(data: QRCode):
    """\f
    Generate a QR code

    Args:
        data (QRCode): QR code generator settings

    Returns:
        QRCodeResponse: The generated QR code in base64 format or

        JSONResponse: Error response
    """
    # Configure
    qr = qrcode.QRCode(version=VERSION, box_size=BOX_SIZE, border=BORDER,
                       error_correction=qrcode.constants.ERROR_CORRECT_L)
    drawer_module = get_drawer_module(data.drawer)

    # Generate
    qr.add_data(data.url)
    qr.make(fit=True)
    buffer = io.BytesIO()
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=drawer_module,
                        color_mask=colormasks.SolidFillColorMask(front_color=data.front_color.as_rgb_tuple(),
                                                                 back_color=data.back_color.as_rgb_tuple()))

    # Saving as data type
    img.save(buffer, format=data.image_type)

    try:
        # Encode base 64 and decode utf-8
        img_base64 = base64.b64encode(buffer.getvalue()).decode(constants.Encoding.UTF8.value)
    except (DataOverflowError, UnicodeDecodeError) as e:
        logger().warning(e.with_traceback)
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={ "errorCode": ErrorCode.QR_ERROR, "error": e.args })

    # Return response
    return QRCodeResponse(result=img_base64)


def get_drawer_module(drawer: DrawerChoices):
    """
    Get drawer module by enum choice

    Args:
        drawer (DrawerChoices): Selected drawer

    Returns:
        ModuleDrawer: Mapped drawer module
    """
    drawer_module = None

    match drawer:
        case DrawerChoices.GAPPEDM:
            drawer_module = moduledrawers.GappedSquareModuleDrawer()
        case DrawerChoices.CIRCLEM:
            drawer_module = moduledrawers.CircleModuleDrawer()
        case DrawerChoices.ROUNDEDM:
            drawer_module = moduledrawers.RoundedModuleDrawer()
        case DrawerChoices.VERTICALM:
            drawer_module = moduledrawers.VerticalBarsDrawer()
        case DrawerChoices.HORIZONTALM:
            drawer_module = moduledrawers.HorizontalBarsDrawer()
        case _:
            drawer_module = moduledrawers.SquareModuleDrawer()
        
    return drawer_module
