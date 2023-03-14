import { helpers } from '@vuelidate/validators'

/**
 * Tiktok Link Regex
 * https://stackoverflow.com/questions/74077377/regular-expression-to-match-any-tiktok-video-id-and-url
 * Cases:
 *   - https://m.tiktok.com/h5/share/usr/<id>.html
 *   - https://m.tiktok.com/v/<id>.html
 *   - https://www.tiktok.com/embed/<id>
 *   - https://www.tiktok.com/share/user/<id>
 *   - https://www.tiktok.com/trending?shareId=<id>
 *   - https://www.tiktok.com/@user/video/<id>?is_copy_url=1&is_from_webapp=v1
 *   - https://www.tiktok.com/@user/video/is_copy_url=1&is_from_webapp=v1&item_id=<id>
 *   - https://vm.tiktok.com/<id>/
 */
export const tikTokLinkRegex = helpers.regex(
    // eslint-disable-next-line no-useless-escape
    /\bhttps?:\/\/(?:m|www|vm)\.tiktok\.com\/(?:.*\b(?:(?:usr|v|embed|user|video)\/|\?shareId=|\&item_id=)(\d+)\b|([\w\d]+))/gm
)
  
/**
 * Twitter Status Regex
 * Cases:
 *   - https://twitter.com/usr/status/<id>?s=24&t=DWBlw1gZk3FFWVQYOHUGYw
 *   - https://mobile.twitter.com/usr/status/<id>
 *   - https://twitter.com/usr/status/<id>
 */
export const twitterStatusRegex = helpers.regex(
  /^https?:\/\/(?:mobile.)?twitter\.com\/(?:#!\/)?(\w+)\/status(?:es)?\/(\d+)(?:\/.*)?(\?(.+))?$/gm
)

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
    return `${minutes} minutes ${seconds} seconds`
  } else {
    return `${seconds} seconds`
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
