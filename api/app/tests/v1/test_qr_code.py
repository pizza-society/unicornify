from fastapi import status
from fastapi.testclient import TestClient

from app.main import app, get_settings
from app.core.docs import qr_code_doc
from app.core.schemas.errors import ErrorCode
from app.tests.v1.test_base import do_test_base_method
from app.v1.constants import SERVICES_ENDPOINT


TEST_ACTION = "/generate-qr-code/"
TEST_URL = f"{ get_settings().API_V1_STR }{ SERVICES_ENDPOINT }{ TEST_ACTION }"

client = TestClient(app)


def test_methods():
    expected_response_post_data = {
        "errorCode": ErrorCode.VALIDATION,
        "errors": {
            "msg": [
                "field required"
            ]
        }
    }

    # run test methods
    do_test_base_method(client, TEST_URL, expected_response_post_data)


def test_generate():
    request_data = {
        "url": "https://www.youtube.com/",
        "imageType": "png",
        "frontColor": "#000000",
        "backColor": "#ffffff",
        "drawer": 1
    }
    expected = qr_code_doc.RESPONSES[status.HTTP_201_CREATED]["content"]["application/json"]["example"]
    response = client.post(TEST_URL, json=request_data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == expected
