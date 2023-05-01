from fastapi import status
from fastapi.testclient import TestClient

from app.main import app, get_settings
from app.core.docs import twitter_video_doc
from app.tests.v1.test_base import do_test_base_method
from app.core.schemas.errors import ErrorCode
from app.v1.constants import SERVICES_ENDPOINT

TEST_ACTION = "/download-tweet-video/"
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


def test_twitter_video_endpoint_with_valid_input():
    """
    Test the Twitter video endpoint with valid input.
    """
    request_data = {
        "url": "https://twitter.com/Xbox/status/1640020986501165058"
    }

    expected = twitter_video_doc.RESPONSES[status.HTTP_200_OK]["content"]["application/json"]["example"]
    response = client.post(TEST_URL, json=request_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


def test_twitter_video_endpoint_with_invalid_input():
    """
    Test the Twitter video endpoint with invalid input.
    """
    request_data = {
        "url": "https://twitter.com/Test123/statux/123445"
    }
    expected = twitter_video_doc.RESPONSES[status.HTTP_422_UNPROCESSABLE_ENTITY]["content"]["application/json"]["example"]

    response = client.post(TEST_URL, json=request_data)
    response_data = response.json()

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response_data == expected
