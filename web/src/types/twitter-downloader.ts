/** Interface for TweetMeta */
export interface TweetMeta {
    /** URL of the tweet */
    tweetUrl: string

    /** ID of the user who uploaded the tweet */
    uploaderUserId: string

    /** Display name of the user who uploaded the tweet */
    uploaderDisplayName: string

    /** Date the tweet was uploaded */
    uploadDate: string

    /** Duration of the tweet media */
    duration: string

    /** URL of the thumbnail for the tweet media */
    thumbnail: string

    /** Title of the tweet */
    title: string

    /** Description of the tweet */
    description: string
}

/** Interface for TweetMedia */
export interface TweetMedia {
    /** Format of the tweet media */
    format: string

    /** Width of the tweet media */
    width: number

    /** Height of the tweet media */
    height: number

    /** Resolution of the tweet media */
    resolution: string

    /** URL of the tweet media */
    url: string

    /** Size of the tweet media */
    size: string
}

/** Interface for TwitterDownloaderResult */
export interface TwitterDownloaderResult {
    /** Meta data for the tweet */
    tweetMetaData: TweetMeta

    /** Array of media information for the tweet */
    tweetMedias: TweetMedia[]

    /** Error message, if any */
    error: string
}

/** Interface for TwitterDownloaderResponse */
export interface TwitterDownloaderResponse {
    /** Result of the Twitter downloader operation */
    result: TwitterDownloaderResult
}
