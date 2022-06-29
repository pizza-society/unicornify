from enum import Enum
from pydantic import BaseModel, HttpUrl
from pydantic.color import Color

class ImageChoices(str, Enum):
    PNG = 'png'
    JPEG = 'jpeg'

class DrawerChoices(int, Enum):
    SQUAREM = 1
    GAPPEDM = 2
    CIRCLEM = 3
    ROUNDEDM = 4
    VERTICALM = 5
    HORIZONTALM = 6

class QRCodeResponse():
    result: str

class QRCodeModel(BaseModel):
    link: HttpUrl
    type: ImageChoices = ImageChoices.PNG
    drawer: DrawerChoices = DrawerChoices.SQUAREM
    front: Color = (0, 0, 0)
    back: Color = (255, 255, 255)

