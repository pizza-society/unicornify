/**
 * DisposableEmailMeta interface defines the structure of
 * an object that represents metadata for a disposable email.
 */
export interface DisposableEmailMeta {
  /** The format of the email, whether it is valid or not. */
  format: boolean

  /** The domain of the email. */
  domain: string

  /** Whether the email is disposable or not. */
  disposable: boolean

  /** Whether the email has a valid DNS or not. */
  dns: boolean

  /** Whether the email is whitelisted or not. */
  whitelist: boolean
}

/** 
 * DisposableEmailResponse interface defines the structure of
 * an object that represents the response from validating a
 * disposable email.
 */
export interface DisposableEmailResponse {
  /** The result of the disposable email validation */
  result: DisposableEmailMeta
}
