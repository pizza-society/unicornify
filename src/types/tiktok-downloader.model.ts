export default interface TikTokDownloaderResponse {
    result: {
        medias : TikTokMedias,
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
    id : {
        format_id: string 
        format_note: string
        vcodec: string
        url: string
        resolution: string
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