import { APIService } from '@/common/api.service'
import { defineStore } from 'pinia'

export const useServiceStore = defineStore('service', {
    state: () => ({}),
    getters: {},
    actions: {
        generateQR(payload: object) {
            return new Promise((resolve, reject) => {
                APIService.post(`services/generate-qr-code`, payload)
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