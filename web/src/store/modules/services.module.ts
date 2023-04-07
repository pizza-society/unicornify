import { defineStore } from 'pinia'

import { APIService } from '@/common/api.service'
import QRGeneratorResponse from '@/types/qr-generator.model'
import DisposableEmailResponse from '@/types/disposable-email-validator.models'
import TwitterDownloaderResponse from '@/types/twitter-downloader.model'
import TikTokDownloaderResponse from '@/types/tiktok-downloader.model'

export const useServiceStore = defineStore('service', {
	state: () => ({}),
	getters: {},
	actions: {
		generateQR(payload: object): Promise<QRGeneratorResponse> {
			return new Promise((resolve, reject) => {
				APIService.post('services/generate-qr-code', payload)
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
				APIService.post('services/validate-disposable-email', payload)
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
				APIService.post('services/download-tweet-video', payload)
					.then(({ data }) => {
						resolve(data)
					})
					.catch(err => {
						reject(err)
					})
			})
		},
		downloadTikTokVideo(payload: object): Promise<TikTokDownloaderResponse> {
			return new Promise((resolve, reject) => {
				APIService.post('services/download-tiktok-video', payload)
					.then(({ data }) => {
						resolve(data)
					})
					.catch(err => {
						reject(err)
					})
			})
		},
		/**
		 * Downloads a Blob file to the browser using the download tag
		 * 
		 * @param {string} url - The URL of the file to be downloaded
		 * @param {string} type - The MIME type of the file to be downloaded
		 * @param {string} fileNamePrefix - The prefix of the generated file name 
		 * @param {boolean} useProxy - A flag indicating whether the link should be passed through the proxy server
		 */
		downloadBlobFile(url: string, type: string, fileNamePrefix: string,
			useProxy = false, query = {}): void {
			/*
			*  Vue/HTML/JS how to download a file to browser using the download tag
			*  https://stackoverflow.com/a/53775165/16711156
			*/
			let targetURL = url

			if (useProxy) {
				targetURL = `${ process.env.VUE_APP_BASE_URL }/services/reverse-proxy/`
			}

			APIService.get(targetURL, null, { responseType: 'blob', params: query })
				.then(response => {
					const blob = new Blob([response.data], { type: type })
					const link = document.createElement('a')
					const timeStamp = new Date().getTime().toString()
					link.href = URL.createObjectURL(blob)
					link.download = `${ fileNamePrefix }-${ timeStamp }`
					link.click()
					URL.revokeObjectURL(link.href)
				})
				.catch(console.error)
		}
	}
})
