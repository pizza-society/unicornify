from fastapi import status
from fastapi.testclient import TestClient


def do_test_base_method(client: TestClient, url: str, expected_response: dict):
    """
    We tests whether only the right methods allowed

    Args:
        client (TestClient): The test client
        url (str): Current URL to test
        expected_response (dict): Expected post data response
    """
    response_get = client.get(url)
    assert response_get.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response_put = client.put(url)
    assert response_put.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response_patch = client.patch(url)
    assert response_patch.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response_delete = client.delete(url)
    assert response_delete.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response_post = client.post(url)
    assert response_post.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response_post.json() == expected_response
