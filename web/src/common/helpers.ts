/**
 * Copies the text to the clipboard.
 * @param {string} text - The text to be copied to the clipboard.
 * @return {Promise} Resolves when the text has been successfully written to the clipboard.
 */
export const copyTextToClipboard = async (text: string): Promise<any> => {
    await navigator.clipboard.writeText(text)
}
