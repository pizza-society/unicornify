from fastapi import status


SUMMARY = "Download TikTok Video"
DESCRIPTION = "Download a TikTok video by providing the video's URL"
RESPONSES = {
    status.HTTP_200_OK: {
        "description": "Fetched",
        "content": {
            "application/json": {
                "example": {
                    "result": {
                        "medias": [
                            {
                                "formatId": "h264_540p_3111210-0",
                                "formatNote": "MP4",
                                "vcodec": "h264",
                                "url": "https://api-h2.tiktokv.com/aweme/v1/play/?video_id=v09044g40000ce8aa53c77u34p1uq6i0&line=0&is_play_url=1&source=PackSourceEnum_FEED&file_id=e18936402da44874a2d49196cda2c24f",
                                "resolution": "576x1024",
                            },
                            {
                                "formatId": "download_addr-0",
                                "formatNote": "MP4 - Watermarked",
                                "vcodec": "h264",
                                "url": "https://api-h2.tiktokv.com/aweme/v1/play/?video_id=v09044g40000ce8aa53c77u34p1uq6i0&line=0&watermark=1&logo_name=tiktok_m&source=FEED&file_id=0d6b4b72ce8947bf8041c9bbfa9b7cac",
                                "resolution": "576x1024",
                            },
                        ],
                        "creator": "JJK Leisure time",
                        "uploader": "user1345259413173",
                        "title": "I love falling asleep to the sound of the rain...do you like it #rainmusic#rainyday#rainsound#relaxingsounds#relaxingmusic#relaxingvideos#relaxingmusic#relaxingvideos#sleepmusic#naturesounds#rainsoundsforsleeping#heavyrain",
                        "description": "I love falling asleep to the sound of the rain...do you like it #rainmusic#rainyday#rainsound#relaxingsounds#relaxingmusic#relaxingvideos#relaxingmusic#relaxingvideos#sleepmusic#naturesounds#rainsoundsforsleeping#heavyrain",
                        "durationString": "11",
                        "mediaType": "video",
                        "format": "bytevc1_720p_1399880-2 - unknown (Playback video)",
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
                            'string does not match regex "\\bhttps?:\\/\\/(?:m|www|vm)\\.tiktok\\.com\\/(?:.*\\b(?:(?:usr|v|embed|user|video)\\/|\\?shareId=|\\&item_id=)(\\d+)\\b|([\\w\\d]+))"'
                        ]
                    },
                }
            }
        },
    },
}
