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
