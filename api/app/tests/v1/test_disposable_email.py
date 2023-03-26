from fastapi import status
from fastapi.testclient import TestClient

from app.main import app, get_settings
from app.v1.constants import SERVICES_ENDPOINT

TEST_ACTION = "/validate-disposable-email/"
TEST_URL = f"{ get_settings().API_V1_STR }{ SERVICES_ENDPOINT }{ TEST_ACTION }"
client = TestClient(app)


def test_disposable_email_methods():
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
                "loc": ["body", "email"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == expected_response_data


def test_disposable_email_endpoint_with_valid_input():
    """
    Test the Disposable Email endpoint with valid input.

    This function tests the Disposable Email endpoint by sending a request with valid email parameters.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: If any of the test cases fail.
    """

    request_data = {"email": "hello@github.com"}
    expected_output = {
        "result": {
            "format": True,
            "domain": "github.com",
            "disposable": False,
            "dns": True,
        }
    }

    response = client.post(TEST_URL, json=request_data)

    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_data == expected_output


def test_disposable_email_endpoint_with_invalid_input():
    """
    Test the Disposable Email endpoint with invalid input.

    This function tests the Disposable Email endpoint by sending a request with an invalid email parameters.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: If any of the test cases fail.
    """
    request_data = {"email": "www.google.com"}
    expected_output = {
        "detail": [
            {
                "loc": ["body", "email"],
                "msg": "value is not a valid email address",
                "type": "value_error.email"
            }
        ]
    }

    response = client.post(TEST_URL, json=request_data)
    response_data = response.json()

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response_data == expected_output
