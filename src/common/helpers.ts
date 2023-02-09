import { helpers } from '@vuelidate/validators'
/**
 * Tiktok Link Regex
 * https://stackoverflow.com/questions/74077377/regular-expression-to-match-any-tiktok-video-id-and-url
 * I.e:
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