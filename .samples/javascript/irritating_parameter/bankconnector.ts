export type OAuthTokenType = string;
export const OAuthToken = 'A really complicated OAuth token that requires calling an external API';

// After start
export abstract class TokenProvider {
  abstract token(): OAuthTokenType;
}

class OAuthTokenProvider extends TokenProvider {
  token(): OAuthTokenType {
    return OAuthToken;
  }
}
// After end

export class BankConnector {

  // After start
  static create(baseUrl: string, provider: TokenProvider): BankConnector {
    return new BankConnector(baseUrl, provider.token());
  }
  // After end

  // Uncomment:  constructor(public baseUrl: string, public token: OAuthTokenType) {
  // After start
  constructor(public baseUrl: string, public token: OAuthTokenType | undefined) {
  // After end
    this.baseUrl = baseUrl;
    this.token = token;
  }

  _buildURL(start: Date, end: Date): string {
    const sstart = start.toISOString().slice(0, 10);
    const send = end.toISOString().slice(0, 10);
    return `${this.baseUrl}rest/merchant/${sstart}/${send}/transactions.csv`;
  }

  getPayments(start: Date, end: Date): string {
    const url = this._buildURL(start, end);
    const headers = { Authorization: `Token ${this.token}` };
    return this.getResponse(url, headers);
  }

  getResponse(url: string, headers: Record<string, string>): string {
    // does nothing in this exercise
    return headers['Authorization'];
  }
}