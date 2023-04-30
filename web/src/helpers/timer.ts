/**
 * Converts a given number to seconds or minutes
 * 
 * @param {string} value - A string representation of a number
 * @return {string} The input number converted to either seconds or minutes, depending on its value
 */
export const convertToTime = (value: string): string => {
	const SECONDS_IN_MINUTE = 60

	const num = parseInt(value)

	if (isNaN(num)) {
		return ''
	}

	const minutes = Math.floor(num / SECONDS_IN_MINUTE)
	const seconds = num % SECONDS_IN_MINUTE

	if (minutes > 0) {
		return `${ minutes } minutes ${ seconds } seconds`
	} else {
		return `${ seconds } seconds`
	}
}

/**
 * Sleep for a given amount
 * 
 * @param {number} time - A number value for the amount of time to sleep
 * @returns {Promise<unknown>} 
 */
export const sleep = (time: number): Promise<unknown> => {
	return new Promise(resolve => setTimeout(resolve, time))
}
