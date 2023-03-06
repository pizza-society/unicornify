export default interface DisposableEmailResponse{
  result:{
    format?: boolean,
    domain?: string,
    disposable?: boolean,
    dns?: boolean
    whitelist?: boolean
  }
}
           