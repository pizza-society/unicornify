/** Base interface for NavbarItem */
export interface NavbarItem {
    /** Nav title */
    title: string,

    /** Nav name */
    name: string

    /** Nav path */
    path?: string,

    /** Nav dropdown links */
    dropdown?: NavbarItemLink[]
}

/** Base interfce for NavbarLink */
export interface NavbarItemLink {
    /** Link path */
    path: string,

    /** Link title */
    title: string
}