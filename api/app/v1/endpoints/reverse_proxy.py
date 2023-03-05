import json
import requests
from http.client import HTTPException

from fastapi import APIRouter, status
from fastapi.responses import Response


router = APIRouter()

@router.get("/reverse-proxy/", summary="Bypass Browser CORS")
def reverse_proxy(url: str):
    """
    Acts as a reverse proxy, allowing cross-origin requests to the specified URL:

        - **url**: the URL to bypass it's CORS
    """
    # Make Request
    response = requests.get(url)
    # Allow CORS access
    response.headers["Access-Control-Allow-Origin"] = "*"

    # Catching error
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Convert byte to dict / json
        error_response = json.loads(e.response.text)
        raise HTTPException(response.status_code,
                            detail=error_response["error"])
    
    return Response(content=response.content,
                    status_code=status.HTTP_200_OK,
                    headers=response.headers)
