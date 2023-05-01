from fastapi import status
from fastapi.testclient import TestClient

from app.main import app, get_settings
from app.core.schemas.errors import ErrorCode
from app.tests.v1.test_base import do_test_base_method
from app.v1.constants import SERVICES_ENDPOINT
from app.core.docs import tiktok_video_doc


TEST_ACTION = "/download-tiktok-video/"
TEST_URL = f"{ get_settings().API_V1_STR }{ SERVICES_ENDPOINT }{ TEST_ACTION }"
client = TestClient(app)

def test_methods():
    """
    Test that the endpoint only accepts allowed HTTP methods.
    """
    expected_response_post_data = {
        "errorCode": ErrorCode.VALIDATION,
        "errors": {
            "msg": [
                "field required"
            ]
        }
    }

    do_test_base_method(client, TEST_URL, expected_response_post_data)


def test_tiktok_video_endpoint_with_valid_input():
    """
    Test the TikTok video endpoint with valid input.
    """
    request_data = {
        "url": "https://www.tiktok.com/@user1345259413173/video/7174417662867442950"
    }
    expected = tiktok_video_doc.RESPONSES[status.HTTP_200_OK]["content"]["application/json"]["example"]

    response = client.post(TEST_URL, json=request_data)
    response_data = response.json()

    # Remove the thumbnail key from the response dictionary, if it exists, as it contains a timestamp which might differ.
    response_data["result"].pop("thumbnail", None)

    assert response.status_code == status.HTTP_200_OK
    assert response_data == expected


def test_tiktok_video_endpoint_with_invalid_input():
    """
    Test the TikTok video endpoint with invalid input.
    """
    request_data = {"url": "https://www.tiktokk.com/@user1234567/video/12345678"}

    expected = tiktok_video_doc.RESPONSES[status.HTTP_422_UNPROCESSABLE_ENTITY]["content"]["application/json"]["example"]

    response = client.post(TEST_URL, json=request_data)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == expected
