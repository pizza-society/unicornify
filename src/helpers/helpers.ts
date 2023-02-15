import { helpers } from '@vuelidate/validators'
/**
 * Tiktok Link Regex
 * https://stackoverflow.com/questions/74077377/regular-expression-to-match-any-tiktok-video-id-and-url
 * Cases:
 *   - https://m.tiktok.com/h5/share/usr/6641141594707361797.html
 *   - https://m.tiktok.com/v/6749869095467945218.html
 *   - https://www.tiktok.com/embed/6567659045795758085
 *   - https://www.tiktok.com/share/user/6567659045795758085
 *   - https://www.tiktok.com/trending?shareId=6744531482393545985
 *   - https://www.tiktok.com/@burntpizza89/video/7067695578729221378?is_copy_url=1&is_from_webapp=v1
 *   - https://www.tiktok.com/@burntpizza89/video/is_copy_url=1&is_from_webapp=v1&item_id=7067695578729221378
 *   - https://vm.tiktok.com/ZMF6rgvXY/
 */
export const tikTokLinkRegex = helpers.regex(
    // eslint-disable-next-line no-useless-escape
    /\bhttps?:\/\/(?:m|www|vm)\.tiktok\.com\/(?:.*\b(?:(?:usr|v|embed|user|video)\/|\?shareId=|\&item_id=)(\d+)\b|([\w\d]+))/gm
  );
  
/**
 * Twitter Status Regex
 * Cases:
 *   - https://twitter.com/tansuyegen/status/1553643510271807489?s=24&t=DWBlw1gZk3FFWVQYOHUGYw
 *   - https://mobile.twitter.com/TheOceanCleanup/status/1551568161018871810
 *   - https://twitter.com/TheOceanCleanup/status/1551568161018871810
 */
export const twitterStatusRegex = helpers.regex(
  /^https?:\/\/(?:mobile.)?twitter\.com\/(?:#!\/)?(\w+)\/status(?:es)?\/(\d+)(?:\/.*)?(\?(.+))?$/gm
);

/**
 * Converts a given number to seconds or minutes
 * 
 * @param {string} value - A string representation of a number
 * @return {string} The input number converted to either seconds or minutes, depending on its value
 */
export const convertToTime = (value: string): string => {
  // Parse the input value as a number
  const num = parseInt(value);

  // Check if the number is greater than or equal to 60
  if (num >= 60) {
      // Convert the number to minutes
      const minutes = Math.floor(num / 60);
      const seconds = num % 60;

      // Return the result as a formatted string
      return `${minutes} minutes ${seconds} seconds`;
  } else {
      // Return the result as a formatted string
      return `${num} seconds`;
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