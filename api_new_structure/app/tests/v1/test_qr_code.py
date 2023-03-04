from fastapi import status
from fastapi.testclient import TestClient

from app.main import app, get_settings
from app.v1.constants import SERVICES_ENDPOINT

TEST_ACTION = "/generate-qr-code/"
TEST_URL = f"{ get_settings().API_V1_STR }{ SERVICES_ENDPOINT }{ TEST_ACTION }"
client = TestClient(app)


def test_methods():
    """
    This test is to show an example.
    We tests whether only the right methods allowed.
    """
    response_get = client.get(TEST_URL)
    assert response_get.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response_put = client.put(TEST_URL)
    assert response_put.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response_patch = client.patch(TEST_URL)
    assert response_patch.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response_delete = client.delete(TEST_URL)
    assert response_delete.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response_post = client.post(TEST_URL)
    expected_response_post_data = {
        "detail": [
            {"loc": ["body"], "msg": "field required", "type": "value_error.missing"}
        ]
    }
    assert response_post.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response_post.json() == expected_response_post_data


def test_generate():
    request_data = {
        "url":"https://www.youtube.com/",
        "imageType":"png",
        "frontColor":"#000000",
        "backColor":"#ffffff",
        "drawer":1
    }
    expected = {
        "result": "iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKCAIAAAD0S4FSAAAFnElEQVR4nO3dQW5jNxRFwSjI/resTDMiDLAZPh5XTRtuy5IOOLng/3y/37+Aor9vvwDgFHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7L+ufWLP5/PrV99yPf7Xfzr+u9d/+w5tz6FnffqRbc+X6c3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkXVutrd1a+azNXFPtvKpzS7tz75Xvxs85vSFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IWvoam2tt4ja2YedW4+5Pe6/Zq7l1pzekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96Q9eRq7bc5tw+beUMYf4rTG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsqzW/ie3nqd5y8yb2H4bpzdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2Q9uVp7cfN0a5f24lM+d7z4ms9xekOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q9bQ1Vrv7rG1czex7ezSbv3s2m/7buxwekOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q9bH3VTz7ey0bu3DfK8mcHpDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUPWtbvWXlxird3aad2682zmXWvnbq3bceu74fSGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oasa3etnVut9Z6JecuLG6+Z36tbnN6QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pD1654QOnOJ5ea5n5v5Cc7k9IYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhqxrTwidaebW6tbzNHf+5x0z3yt3rQGDyBuy5A1Z8oYseUOWvCFL3pAlb8iSN2Q9+YTQHTMXYDtefFU7Zi7t1m59Ck5vyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IGrpau7VMmvlurJ179ugtM5eFM9eBa05vyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IuvaE0Jkrn7Vbu6Vbu7Sd3zvzWasvLhp3OL0hS96QJW/IkjdkyRuy5A1Z8oYseUOWvCHr2mrtRbdu6rq1tXpxl7a28z67aw0YRN6QJW/IkjdkyRuy5A1Z8oYseUOWvCFr6BNCd9xaU83ch818EuuLZu7S1pzekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QdW219tucu2tt5krvxdfc4/SGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oasa08I7d3UtV5EzdxLzfwULM/+FKc3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkXVutrc1cJu1svHZ+9tYTQm9t2m7dxLZj5jfW6Q1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVlDV2trve2R9dh8M3dpa05vyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IenK19qJzm6dzi7eZ98Pd+r23XtUOpzdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2RZrT1g5k1sO2bu0nbe55k3sTm9IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwh68nV2syF0Nq5ndatTdvOp7Dzms/9RS/u/9ac3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekDV0tdbbD629eJvaubvHbq0Szz1N1RNCgT9M3pAlb8iSN2TJG7LkDVnyhix5Q5a8Ievz4r1lwE84vSFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGrH8BffNzoWyqfQ8AAAAASUVORK5CYII="
    }
    response = client.post(TEST_URL, json=request_data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == expected
