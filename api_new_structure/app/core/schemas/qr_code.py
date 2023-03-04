from enum import Enum
from pydantic import HttpUrl
from pydantic.color import Color

from .base import BaseResponse
from .camel_case import CamelModel

class ImageChoices(str, Enum):
    """ Image choices for QR code generator """

    PNG = "png"
    JPEG = "jpeg"


class DrawerChoices(int, Enum):
    """ Drawer choices for QR code generator """

    SQUAREM = 1
    GAPPEDM = 2
    CIRCLEM = 3
    ROUNDEDM = 4
    VERTICALM = 5
    HORIZONTALM = 6


class QRCodeResponse(BaseResponse):
    """ QR code generator response """

    pass


class QRCode(CamelModel):
    """ QR code model """

    url: HttpUrl
    image_type: ImageChoices = ImageChoices.PNG # PNG file type
    drawer: DrawerChoices = DrawerChoices.SQUAREM
    front_color: Color = Color("rgb(0, 0, 0)") # black
    back_color: Color = Color("rgb(255, 255, 255)") # white
