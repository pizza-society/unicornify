/** Interface for TikTokMedia */
export interface TikTokMedia {
    /** The format id of the media */
    formatId: string 

    /** The format note of the media */
    formatNote: string

    /** The vcodec of the media */
    vcodec: string

    /** The url of the media */
    url: string

    /** The resolution of the media */
    resolution: string
}

/** Interface for TikTokMeta */
export interface TikTokMeta {
    /** The name of the creator */
    creator: string

    /** The name of the uploader */
    uploader: string

    /** The title of the video */
    title: string

    /** The description of the video */
    description: string

    /** The duration of the video in string format */
    durationString: string

    /** The type of the video */
    type: string

    /** The thumbnail of the video */
    thumbnail: string

    /** The format of the video */
    format: string

    /** An error message if there is any */
    error: string
}

/** Interface for TikTokDownloaderResult */
export interface TikTokDownloaderResult extends TikTokMeta {
    /** Array of the media data of the video */
    medias: TikTokMedia[]
}

/** Interface for TikTokDownloaderResponse */
export interface TikTokDownloaderResponse {
    /** The result of the TikTok downloader */
    result: TikTokDownloaderResult
}
