from fastapi import status
from fastapi.testclient import TestClient

from app.main import app, get_settings
from app.v1.constants import SERVICES_ENDPOINT

TEST_ACTION = "/download-tweet-video/"
TEST_URL = f"{ get_settings().API_V1_STR }{ SERVICES_ENDPOINT }{ TEST_ACTION }"
client = TestClient(app)


def test_twitter_video_methods():
    """
    Test that the endpoint only accepts allowed HTTP methods.
    """

    # Test GET method
    response = client.get(TEST_URL)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    # Test PUT method
    response = client.put(TEST_URL)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    # Test PATCH method
    response = client.patch(TEST_URL)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    # Test DELETE method
    response = client.delete(TEST_URL)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    # Test POST method with missing required field
    request_data = {}
    response = client.post(TEST_URL, json=request_data)
    expected_response_data = {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == expected_response_data


def test_twitter_video_endpoint_with_valid_input():
    """
    Test the Twitter video endpoint with valid input.
    """

    request_data = {
        "url": "https://twitter.com/Xbox/status/1640020986501165058"
    }
    expected_output = {
        "result": {
            "tweetMetaData": {
                "tweetUrl": "https://twitter.com/Xbox/status/1640020986501165058",
                "uploaderUserId": "Xbox",
                "uploaderDisplayName": "Xbox",
                "uploadDate": "26-03-2023",
                "duration": "0:00:10",
                "thumbnail": "https://pbs.twimg.com/media/FsKGYJPWIAAkQ2i.jpg?name=orig",
                "title": "Xbox - https://t.co/cXPXo68Ieq",
                "description": "https://t.co/cXPXo68Ieq",
            },
            "tweetMedias": [
                {
                    "format": "http-432 - 320x320",
                    "width": 320,
                    "height": 320,
                    "resolution": "320 x 320",
                    "url": "https://video.twimg.com/amplify_video/1640020879806550018/vid/320x320/CuQ0RG3hOAr4neg9.mp4?tag=16",
                    "size": "N/A",
                },
                {
                    "format": "http-832 - 540x540",
                    "width": 540,
                    "height": 540,
                    "resolution": "540 x 540",
                    "url": "https://video.twimg.com/amplify_video/1640020879806550018/vid/540x540/UzdhD_F2tgOdTHY4.mp4?tag=16",
                    "size": "N/A",
                },
                {
                    "format": "http-1280 - 720x720",
                    "width": 720,
                    "height": 720,
                    "resolution": "720 x 720",
                    "url": "https://video.twimg.com/amplify_video/1640020879806550018/vid/720x720/XnPHB9v3rX8Ch99-.mp4?tag=16",
                    "size": "N/A",
                },
                {
                    "format": "http-8768 - 1080x1080",
                    "width": 1080,
                    "height": 1080,
                    "resolution": "1080 x 1080",
                    "url": "https://video.twimg.com/amplify_video/1640020879806550018/vid/1080x1080/LwPechuE0z3_L8Ut.mp4?tag=16",
                    "size": "N/A",
                },
            ],
        }
    }

    response = client.post(TEST_URL, json=request_data)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_data == expected_output


def test_twitter_video_endpoint_with_invalid_input():
    """
    Test the Twitter video endpoint with invalid input.
    """
    request_data = {
        "url": "https://twitter.com/Test123/statux/123445"
    }
    expected_output = {
        "detail": [
            {
                "loc": ["body", "url"],
			    "msg": "string does not match regex \"^https?:\\/\\/(?:mobile.)?twitter\\.com\\/(?:#!\\/)?(\\w+)\\/status(?:es)?\\/(\\d+)(?:\\/.*)?(\\?(.+))?$\"",
                "type": "value_error.str.regex",
                "ctx": {
                    "pattern": "^https?:\\/\\/(?:mobile.)?twitter\\.com\\/(?:#!\\/)?(\\w+)\\/status(?:es)?\\/(\\d+)(?:\\/.*)?(\\?(.+))?$"
                },
            }
        ]
    }

    response = client.post(TEST_URL, json=request_data)
    response_data = response.json()

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response_data == expected_output
