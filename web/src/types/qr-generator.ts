/** Image format choices for QR generator */
export enum ImageChoices {
    PNG = 'png',
    JPEG = 'jpeg'
}

/** QR generator drawer module choices */
export enum DrawerChoices {
    SQUAREM = 1,
    GAPPEDM = 2,
    CIRCLEM = 3,
    ROUNDEDM = 4,
    VERTICALM = 5,
    HORIZONTALM = 6
}

/** QR generator response interface */
export interface QRGeneratorResponse {
	result: string
}