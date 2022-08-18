from enum import Enum

from humps import camelize
from pydantic import BaseModel, Field, HttpUrl
from pydantic.color import Color

def to_camel_case(string):
    return camelize(string)

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

class CamelModel(BaseModel):
    """
        Base model with snake_case to camelCase conversion
    """
    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True

class QRCodeResponse(BaseModel):
    result: str

class QRCodeModel(CamelModel):
    url: HttpUrl
    image_type: ImageChoices = ImageChoices.PNG
    drawer: DrawerChoices = DrawerChoices.SQUAREM
    front_color: Color = Color('rgb(0, 0, 0)')
    back_color: Color = Color('rgb(255, 255, 255)')

class TwitterVideoDownloaderModel(BaseModel):
    url: HttpUrl

class TwitterVideoDownloaderResponse(BaseModel):
    result: object