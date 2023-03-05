import json
import requests
from http.client import HTTPException

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.core.schemas.disposable_email import DisposableEmailSchema, DisposableEmailResponse


router = APIRouter()

@router.post("/validate-disposable-email/",
             response_model=DisposableEmailResponse,
             summary="Validate disposable email")
def validate_disposable_email(data: DisposableEmailSchema):
    """
    TODO: Update docstring format
    Validate disposable Email by using 3rd party API with all the information:

    - **email**: a valid email address

    Documentation about the external API can be found here https://www.disify.com/
    """
    BASE_URL = f"https://www.disify.com/api/email"

    # Make request
    disposable_email_service = requests.get(f"{BASE_URL}/{data.email}")

    # Catching error
    try:
        disposable_email_service.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Convert byte to dict / json
        error_response = json.loads(e.response.text)
        raise HTTPException(disposable_email_service.status_code,
                            detail=error_response["error"])
    
    # Return response
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={ "result": disposable_email_service.json() })
