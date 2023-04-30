import { defineStore } from 'pinia'

import { ToastChildItem, TOAST_TIMEOUT } from '@/types/toast'

export const useToastStore = defineStore('toast', {
	state: () => {
		return {
			closable: true as boolean,
			timeout: TOAST_TIMEOUT as number,
			notificationList: [] as ToastChildItem[]
		}
	},
	getters: {},
	actions: {
		info(text: string) {
			// Prepare toast
			const prepared: ToastChildItem = {
				id: this.notificationList.length === 0
					? 0
					: this.notificationList[this.notificationList.length - 1]?.id + 1,
				theme: 'info',
				text: text
				
			}

			// Trigger list update
			this.appendList(prepared)
		},
		success(text: string) {
			// Prepare toast
			const prepared: ToastChildItem = {
				id: this.notificationList.length === 0
					? 0
					: this.notificationList[this.notificationList.length - 1]?.id + 1,
				theme: 'success',
				text: text
				
			}

			// Trigger list update
			this.appendList(prepared)
		},
		error(text: string) {
			// Prepare toast
			const prepared: ToastChildItem = {
				id: this.notificationList.length === 0
					? 0
					: this.notificationList[this.notificationList.length - 1]?.id + 1,
				theme: 'error',
				text: text
				
			}

			// Trigger list update
			this.appendList(prepared)
		},
		warning(text: string) {
			// Prepare toast
			const prepared: ToastChildItem = {
				id: this.notificationList.length === 0
					? 0
					: this.notificationList[this.notificationList.length - 1]?.id + 1,
				theme: 'warning',
				text: text
				
			}

			// Trigger list update
			this.appendList(prepared)
		},
		appendList(prepared: ToastChildItem) {
			// Update list
			this.notificationList.push(prepared)

			// Start toast timer
			const currentInterval = setTimeout(
				() => {
					this.remove(prepared.id)
					clearTimeout(currentInterval)
				}, this.timeout
			)
		},
		remove(id: number) {
			const indexFinder = (el: ToastChildItem) => el.id === id
			const toRemoveIndex = this.notificationList.findIndex(indexFinder)

			if (toRemoveIndex > -1) {
				this.notificationList.splice(toRemoveIndex, 1)
			}
			return this.notificationList
		}
	}
})