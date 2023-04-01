from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import http_exception_handler
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from app.core.schemas.errors import ErrorCode
from app.core.schemas.validations import ErrorKey, LocKey, ValidationErrorType


DEFAULT_KEY = "msg"


class ValidationMessage:
    """ Validation message is generated here """

    NONE_NOT_ALLOWED_TEXT = "Null is not allowed"
    NOT_VALID_COLOR = "Not a valid color"

    def __init__(self, errors):
        self.errors = errors
        self.error_body = { }

    def _get_field_name(self, err):
        loc = err.get(ErrorKey.LOC, None)
        possible_locs = (LocKey.BODY, LocKey.PATH, LocKey.QUERY)
        filtered_locs = loc[1:] if loc[0] in possible_locs else loc
        name = ".".join(filtered_locs) # nested fields with dot-notation

        # return msg key if no field name
        return DEFAULT_KEY if not name else name

    def _get_field_errors(self, err):
        field_name = self._get_field_name(err)
        field_errors = self._map_error(err)

        return { f"{ field_name }": field_errors }
    
    def _map_error(self, err):
        messages = []
        error_type = err.get(ErrorKey.TYPE, None)

        match error_type:
            case ValidationErrorType.URL:
                messages = self._get_url_errors(err)
            case ValidationErrorType.ENUM:
                messages = self._get_enum_errors(err)
            case ValidationErrorType.NONE_TYPE:
                messages = [self.NONE_NOT_ALLOWED_TEXT]
            case ValidationErrorType.COLOR:
                messages = [self.NOT_VALID_COLOR]
            case _:
                messages = [err.get(ErrorKey.MSG, "")]

        return messages
    
    def _get_url_errors(self, err):
        field_messages = []
        allowed_values = err.get("ctx", {}).get("allowed_schemes", None)
        msg = "Not a valid URL"

        if allowed_values:
            choices = str(allowed_values).replace("{", "")\
                                         .replace("}", "")
            msg = f"URL scheme not valid. Allowed schemes: { choices }"

        field_messages.append(msg)
        return field_messages
    
    def _get_enum_errors(self, err):
        field_messages = []
        default_error = err.get(ErrorKey.MSG, "")
        text_separator = "permitted: "
        splitted_str = str(default_error).split(text_separator, maxsplit=1)[1]

        msg = f"Not a valid choice. Allowed choices: { splitted_str }"
        field_messages.append(msg)

        return field_messages
    
    def transform_message(self):
        for err in self.errors:
            self.error_body.update(self._get_field_errors(err))
        
        return self.error_body


async def custom_http_exception_handler(request: Request,
                                        exc: HTTPException) -> Response:
    """
    Override default http exception handler. Just a placeholder, can use it in the future

    Args:
        request (Request): the HTTP request
        exc (HTTPException): the HTTP exception

    Returns:
        Response: default response
    """

    return await http_exception_handler(request, exc)


async def validation_exception_handler(request: Request,
                                       exc: RequestValidationError) -> JSONResponse:
    """
    Override default validation exception handler. Transforms response content
    to different format.

    Args:
        request (Request): the HTTP request
        exc (RequestValidationError): the request validation error

    Returns:
        JSONResponse: a custom content JSON response
    
    """

    error_body = ValidationMessage(errors=exc.errors()).transform_message()
    response_content = { "errorCode": ErrorCode.VALIDATION,
                         "errors": jsonable_encoder(error_body) }

    return JSONResponse(status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                        content=response_content)
