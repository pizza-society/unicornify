from fastapi import APIRouter

import io
import base64
import qrcode

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

from app.services.models import DrawerChoices, QRCodeModel

router = APIRouter()

@router.post('/generate-qr-code/')
def generate_qr(data: QRCodeModel):
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
    qr.add_data(data.link)
    qr.make(fit=True)
    buffer = io.BytesIO()
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=drawer_module,
        color_mask=SolidFillColorMask(
            front_color=data.front.as_rgb_tuple(),
            back_color=data.back.as_rgb_tuple()
        )
    )

    # Saving as data type
    img.save(buffer, format=data.type)

    # Encode base 64 and decode utf-8
    img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return img_base64

