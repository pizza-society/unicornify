import { APIService } from '@/common/api.service'
import QRGeneratorResponse from '@/types/qr-generator.model'
import DisposableEmailResponse from '@/types/disposable-email-validator.models'
import TwitterDownloaderResponse from '@/types/twitter-downloader.model'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useServiceStore = defineStore('service', {
    state: () => ({}),
    getters: {},
    actions: {
        generateQR(payload: object): Promise<QRGeneratorResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`services/generate-qr-code`, payload)
                    .then(({ data }) => {
                        resolve(data)
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        validateDisposableEmail(payload: object): Promise<DisposableEmailResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`services/validate-disposable-email`, payload)
                    .then(({ data }) => {
                        resolve(data)
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        downloadTwitterVideo(payload: object): Promise<TwitterDownloaderResponse> {
            return new Promise((resolve, reject) => {
                APIService.post(`services/download-tweet-video`, payload)
                    .then(({ data }) => {
                        resolve(data)
                    })
                    .catch(err => {
                        reject(err)
                    })
            }) 
        },
        downloadBlobFile(url: string, type: string, fileNamePrefix: string): void
        {
            /*
            *  Vue/HTML/JS how to download a file to browser using the download tag
            *  https://stackoverflow.com/a/53775165/16711156
            */
            axios.get(url, { responseType: 'blob' })
                .then(response => {
                    const blob = new Blob([response.data], { type: type })
                    const link = document.createElement('a')
                    const timeStamp = new Date().getTime().toString();
                    link.href = URL.createObjectURL(blob)
                    link.download = `${fileNamePrefix}-${timeStamp}`
                    link.click()
                    URL.revokeObjectURL(link.href)
                })
                .catch(console.error)
        }
    },
})
