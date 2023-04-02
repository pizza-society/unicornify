from fastapi import status
from fastapi.testclient import TestClient

from app.main import app, get_settings
from app.tests.v1.test_base import do_test_base_method
from app.core.docs import disposable_email_doc
from app.core.schemas.errors import ErrorCode
from app.v1.constants import SERVICES_ENDPOINT

TEST_ACTION = "/validate-disposable-email/"
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


def test_disposable_email_endpoint_with_valid_input():
    """
    Test the Disposable Email endpoint with valid input.
    """

    request_data = {
        "email": "hello@github.com"
    }
    expected = disposable_email_doc.RESPONSES[status.HTTP_200_OK]["content"]["application/json"]["example"]
    response = client.post(TEST_URL, json=request_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


def test_disposable_email_endpoint_with_invalid_input():
    """
    Test the Disposable Email endpoint with invalid input.
    """

    request_data = {
        "email": "www.google.com"
    }

    expected = disposable_email_doc.RESPONSES[status.HTTP_422_UNPROCESSABLE_ENTITY]["content"]["application/json"]["example"]
    response = client.post(TEST_URL, json=request_data)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == expected
