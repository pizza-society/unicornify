from fastapi import status
from fastapi.testclient import TestClient

from app.main import app, get_settings
from app.v1.constants import SERVICES_ENDPOINT

TEST_ACTION = "/download-tiktok-video/"
TEST_URL = f"{ get_settings().API_V1_STR }{ SERVICES_ENDPOINT }{ TEST_ACTION }"
client = TestClient(app)


def test_tiktok_video_methods():
    """
    Test that the endpoint only accepts allowed HTTP methods.

    This test function makes requests to the endpoint with various HTTP methods to verify that
    only the expected methods are allowed. It also tests the behavior when a required field is missing
    in the request payload.

    Returns:
        None

    Raises:
        AssertionError: If any of the test cases fail.
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


def test_tiktok_video_endpoint_with_valid_input():
    """
    Test the TikTok video endpoint with valid input.

    This function tests the TikTok video endpoint by sending a request with valid input parameters.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: If any of the test cases fail.
    """
    # test code goes here

    request_data = {
        "url": "https://www.tiktok.com/@user1345259413173/video/7174417662867442950"
    }
    expected_output = {
        "result": {
            "medias": [
                {
                    "formatId": "h264_540p_3111210-0",
                    "formatNote": "MP4",
                    "vcodec": "h264",
                    "url": "https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/play/?video_id=v09044g40000ce8aa53c77u34p1uq6i0&line=0&is_play_url=1&source=PackSourceEnum_FEED&file_id=e18936402da44874a2d49196cda2c24f",
                    "resolution": "576x1024",
                },
                {
                    "formatId": "download_addr-0",
                    "formatNote": "MP4 - Watermarked",
                    "vcodec": "h264",
                    "url": "https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/play/?video_id=v09044g40000ce8aa53c77u34p1uq6i0&line=0&watermark=1&logo_name=tiktok_m&source=FEED&file_id=0d6b4b72ce8947bf8041c9bbfa9b7cac",
                    "resolution": "576x1024",
                },
            ],
            "creator": "JJK Leisure time",
            "uploader": "user1345259413173",
            "title": "I love falling asleep to the sound of the rain...do you like it #rainmusic#rainyday#rainsound#relaxingsounds#relaxingmusic#relaxingvideos#relaxingmusic#relaxingvideos#sleepmusic#naturesounds#rainsoundsforsleeping#heavyrain",
            "description": "I love falling asleep to the sound of the rain...do you like it #rainmusic#rainyday#rainsound#relaxingsounds#relaxingmusic#relaxingvideos#relaxingmusic#relaxingvideos#sleepmusic#naturesounds#rainsoundsforsleeping#heavyrain",
            "durationString": "11",
            "type": "video",
            "format": "bytevc1_720p_1399880-2 - unknown (Playback video)",
        }
    }

    response = client.post(TEST_URL, json=request_data)
    response_data = response.json()

    # Remove the thumbnail key from the response dictionary, if it exists, as it contains a timestamp which might differ.
    response_data["result"].pop("thumbnail", None)

    assert response.status_code == status.HTTP_200_OK
    assert response_data == expected_output


def test_tiktok_video_endpoint_with_invalid_input():
    """
    Test the TikTok video endpoint with invalid input.

    This function tests the TikTok video endpoint by sending a request with an invalid URL input parameters.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: If any of the test cases fail.
    """
    request_data = {"url": "https://www.tiktokk.com/@user1234567/video/12345678"}
    expected_output = {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": 'string does not match regex "\\bhttps?:\\/\\/(?:m|www|vm)\\.tiktok\\.com\\/(?:.*\\b(?:(?:usr|v|embed|user|video)\\/|\\?shareId=|\\&item_id=)(\\d+)\\b|([\\w\\d]+))"',
                "type": "value_error.str.regex",
                "ctx": {
                    "pattern": "\\bhttps?:\\/\\/(?:m|www|vm)\\.tiktok\\.com\\/(?:.*\\b(?:(?:usr|v|embed|user|video)\\/|\\?shareId=|\\&item_id=)(\\d+)\\b|([\\w\\d]+))"
                },
            }
        ]
    }

    response = client.post(TEST_URL, json=request_data)
    response_data = response.json()

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response_data == expected_output
