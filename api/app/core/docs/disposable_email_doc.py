from fastapi import status


SUMMARY = "Validate Email"
DESCRIPTION = "Check whether an Email is disposable or not."
RESPONSES = {
    status.HTTP_200_OK: {
        "description": "Checked",
        "content": {
            "application/json": {
                "example": {
                    "result": {
                        "format": True,
                        "domain": "github.com",
                        "disposable": False,
                        "dns": True,
                    }
                }
            }
        },
    },
    status.HTTP_422_UNPROCESSABLE_ENTITY: {
        "description": "Unable to check",
        "content": {
            "application/json": {
                "example": {
                    "errorCode": "validation_error",
                    "errors": {
                        "email": [
                            "value is not a valid email address"
                        ]
                    }
                }
            }
        },
    }
}
