from fastapi import status


SUMMARY = "Twitter Video Downloader"
DESCRIPTION = "Download Twitter videos by providing the tweet URL. The API will return a JSON object with metadata about the tweet and its available video formats with download URLs."
RESPONSES = {
    status.HTTP_200_OK: {
        "description": "Fetched",
        "content": {
            "application/json": {
                "example": {
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
            }
        },
    },
    status.HTTP_422_UNPROCESSABLE_ENTITY: {
        "description": "Unable to fetch",
        "content": {
            "application/json": {
                "example": {
                    "errorCode": "validation_error",
                    "errors": {
                        "url": [
                            'string does not match regex "^https?:\\/\\/(?:mobile.)?twitter\\.com\\/(?:#!\\/)?(\\w+)\\/status(?:es)?\\/(\\d+)(?:\\/.*)?(\\?(.+))?$"'
                        ]
                    },
                }
            }
        },
    },
}
