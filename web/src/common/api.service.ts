import axios, { AxiosRequestConfig } from 'axios'

export const APIService = {
	// Config
	init() {
		// URL configs
		axios.defaults.baseURL = `${ import.meta.env.VITE_BASE_URL }`

		// Error interceptors
		axios.interceptors.response.use(undefined, (error) => {
			const { response } = error
			if (!response) {
				// Network
				if (process.env.NODE_ENV === 'development') {
					console.error(error)
				}
				
				return
			}

			if ([401, 403].includes(response.status)) {
				// if 401 or 403 response returned from api
				// example: https://jasonwatmore.com/post/2020/10/06/vue-3-facebook-login-tutorial-example#error-interceptor-js
			}

			// const errorMessage = response.data?.message || response.statusText // uncomment this to show shorter error
			const errorMessage = response // show all
			if (process.env.NODE_ENV === 'development') {
				console.error('ERROR:', JSON.stringify(errorMessage))
			}
			
			if (response.data) {
				// alert(response.data.detail)
				// console.log('Interceptor detail: ', response.data.detail)
			}

			return Promise.reject(response)
		})
	},
	setHeader() {
		// axios.defaults.headers.
	},
	async get(resource: string, query: string | null = null, options?: AxiosRequestConfig) {
		const url = query ? `${ resource }/?${ query }` : resource

		return await axios.get(url, options).catch(error => {
			throw error
		})
	},
	async post(resource: string, params: object) {
		return await axios.post(`${ resource }/`, params).catch(error => {
			// console.log(error)
			throw error
		})
	}
}