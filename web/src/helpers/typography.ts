/** A text concatter */
export const TextConcat = (base: string, textVar: string, textRepl: string) => {
	return base.replace(textVar, textRepl)
}