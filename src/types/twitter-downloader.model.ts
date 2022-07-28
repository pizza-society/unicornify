export default interface TwitterDownloaderResponse{
    result: {
        tweet_meta_data: {
            tweet_url: string,
            uploader_user_id: string,
            uploader_display_name: string,
            upload_date: string,
            duration: string,
            thumbnail: string,
            title: string,
            description: string
        },
        tweet_medias: object
    }
}