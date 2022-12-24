export default interface TikTokDownloaderResponse {
    result: {
        medias ? : {
            index: TikTokMedias
        },
        creator?: string,
        uploader?: string,
        title?: string,
        description?: string,
        duration_string?: string,
        _type?: string,
        thumbnail?: string,
        format?: string,
        error?: string,
    }
}

export interface TikTokMedias {
    id ? : {
        format_id: string | null | undefined
        format_note: string | null | undefined
        vcodec: string | null | undefined
        url: string | null | undefined
        resolution: string | null | undefined
    }
}


export interface TikTokMeta {
    creator?: string,
    uploader?: string,
    title?: string,
    description?: string,
    duration_string?: string,
    _type?: string,
    thumbnail?: string,
    format?: string,
    error?: string,
}