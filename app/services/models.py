from pydantic import BaseModel, HttpUrl

class QRCodeResponse():
    result: str

class QRCodeModel(BaseModel):
    link: HttpUrl