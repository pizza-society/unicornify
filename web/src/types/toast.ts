/** Toast default timeout in milliseconds */
export const TOAST_TIMEOUT = 3000

/** Toast theme types */
export type ToastType = 'info' | 'success' | 'error' | 'warning'

/** Base interface for ToastChild component */
export interface ToastChildItem {
    /** item id */
    id: number

    /** item toast type */
    theme: ToastType

    /** item text */
    text: string
}

/** Toast icon map to theme */
export const ToastIconMap = {
	info: 'fa-solid fa-info fa-xs',
	success: 'fa-solid fa-check fa-xs',
	error: 'fa-solid fa-triangle-exclamation fa-xs',
	warning: 'fa-solid fa-exclamation fa-xs'
}

/** Toast color map to theme */
export const ToastColorMap = {
	info: 'toast-info',
	success: 'toast-success',
	error: 'toast-error',
	warning: 'toast-warning'
}