from fastapi import status


SUMMARY = "Generate a QR code"
DESCRIPTION = "Generate a QR code with all the information; url, image_type, drawer, frontColor, backColor"
RESPONSES = {
    status.HTTP_200_OK: {
        "description": "Generated",
        "content": {
            "application/json": {
                "example": {
                    "result": (
                        "iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKCAIAAAD0S4FSAAAFnElEQVR4nO3dQW5jNxRF"
                        "wSjI/resTDMiDLAZPh5XTRtuy5IOOLng/3y/37+Aor9vvwDgFHlDlrwhS96QJW/Ikjdk"
                        "yRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQN"
                        "WfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7L+ufWLP5/P"
                        "rV99yPf7Xfzr+u9d/+w5tz6FnffqRbc+X6c3ZMkbsuQNWfKGLHlDlrwhS96QJW/Ikjdk"
                        "XVutrd1a+azNXFPtvKpzS7tz75Xvxs85vSFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IWvo"
                        "am2tt4ja2YedW4+5Pe6/Zq7l1pzekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96Q9eRq7bc5"
                        "tw+beUMYf4rTG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsqzW/ie3nqd5y8yb2H4bpzdk"
                        "yRuy5A1Z8oYseUOWvCFL3pAlb8iSN2Q9uVp7cfN0a5f24lM+d7z4ms9xekOWvCFL3pAl"
                        "b8iSN2TJG7LkDVnyhix5Q9bQ1Vrv7rG1czex7ezSbv3s2m/7buxwekOWvCFL3pAlb8iS"
                        "N2TJG7LkDVnyhix5Q9bH3VTz7ey0bu3DfK8mcHpDlrwhS96QJW/IkjdkyRuy5A1Z8oYs"
                        "eUPWtbvWXlxird3aad2682zmXWvnbq3bceu74fSGLHlDlrwhS96QJW/IkjdkyRuy5A1Z"
                        "8oasa3etnVut9Z6JecuLG6+Z36tbnN6QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pD1654Q"
                        "OnOJ5ea5n5v5Cc7k9IYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhqxrTwidaebW6tbzNHf+"
                        "5x0z3yt3rQGDyBuy5A1Z8oYseUOWvCFL3pAlb8iSN2Q9+YTQHTMXYDtefFU7Zi7t1m59"
                        "Ck5vyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IGrpau7VMmvlurJ179ugtM5eFM9eBa05v"
                        "yJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IuvaE0Jkrn7Vbu6Vbu7Sd3zvzWasvLhp3OL0h"
                        "S96QJW/IkjdkyRuy5A1Z8oYseUOWvCHr2mrtRbdu6rq1tXpxl7a28z67aw0YRN6QJW/I"
                        "kjdkyRuy5A1Z8oYseUOWvCFr6BNCd9xaU83ch818EuuLZu7S1pzekCVvyJI3ZMkbsuQN"
                        "WfKGLHlDlrwhS96QdW219tucu2tt5krvxdfc4/SGLHlDlrwhS96QJW/IkjdkyRuy5A1Z"
                        "8oasa08I7d3UtV5EzdxLzfwULM/+FKc3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkXVut"
                        "rc1cJu1svHZ+9tYTQm9t2m7dxLZj5jfW6Q1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVlD"
                        "V2trve2R9dh8M3dpa05vyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IenK19qJzm6dzi7eZ"
                        "98Pd+r23XtUOpzdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2RZrT1g5k1sO2bu0nbe55k3"
                        "sTm9IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwh68nV2syF0Nq5ndatTdvOp7Dzms/9RS/u"
                        "/9ac3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekDV0tdbbD629eJvaubvHbq0Szz1N1RNC"
                        "gT9M3pAlb8iSN2TJG7LkDVnyhix5Q5a8Ievz4r1lwE84vSFL3pAlb8iSN2TJG7LkDVny"
                        "hix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOW"
                        "vCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGrH8BffNzoWyq"
                        "fQ8AAAAASUVORK5CYII="
                    )
                }
            }
        }
    }
}
