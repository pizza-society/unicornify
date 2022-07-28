import { APIService } from '@/common/api.service'
import QRGeneratorResponse from '@/types/qr-generator.model'
import DisposableEmailResponse from '@/types/disposable-email-validator.models'
import TwitterDownloaderResponse from '@/types/twitter-downloader.model'
import { defineStore } from 'pinia'

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
        }
    },
})
