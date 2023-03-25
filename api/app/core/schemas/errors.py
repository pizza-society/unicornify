from enum import Enum


class ErrorCode(str, Enum):
    """
    Error code related to services
    """
    # FastAPI related
    VALIDATION = "validation_error"

    # QR code related
    QR_ERROR = "qr_error"
    