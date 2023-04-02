from enum import Enum


class ValidationErrorType(str, Enum):
    """ Validation error types """

    URL = "value_error.url.scheme"
    ENUM = "type_error.enum"
    NONE_TYPE = "type_error.none.not_allowed"
    COLOR = "value_error.color"


class ErrorKey(str, Enum):
    """ Error key types """

    LOC = "loc"
    MSG = "msg"
    TYPE = "type"


class LocKey(str, Enum):
    """ Loc key types """

    BODY = "body"
    PATH = "path"
    QUERY = "query"  
