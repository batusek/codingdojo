import { expect, test } from 'vitest';
import { BankConnector, OAuthTokenType, OAuthToken } from './bankconnector';


test('should build URL with no token', () => {
    const connector = new BankConnector('https://api.mybank.cz/', null);
    const url = connector._buildURL(new Date(2024, 0, 1), new Date(2024, 0, 31));
    expect(url).toBe('https://api.mybank.cz/rest/merchant/2024-01-01/2024-01-31/transactions.csv');
});

test('should return Authorization header', () => {
    const connector = new BankConnector('https://api.mybank.cz/', OAuthToken);
    const response = connector.getPayments(new Date(2024, 0, 1), new Date(2024, 0, 31));
    expect(response).toBe('Token A really complicated OAuth token that requires calling an external API');
});

