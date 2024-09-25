from datetime import datetime
import os
import unittest

from irritating_parameter.bankconnector import *

# After start
class TestTokenProvider(TokenProvider):
    def __init__(self, token: str):
        self.token = token
        
    def token(self) -> OAuthTokenType:
        return self.token
# After end


class BankConnectorTest(unittest.TestCase):
    def test_build_url(self):
        """ TODO: write a test that test the buildURL method by providing None for token """
        # After start
        connector = BankConnector("https://api.mybank.cz/", None)
        url = connector._buildURL(datetime(2024,1,1),datetime(2024,1,31))
        self.assertEqual(url, "https://api.mybank.cz/rest/merchant/2024-01-01/2024-01-31/transactions.csv")
        # After end

    def test_get_payments(self):
        """ TODO: rewrite the test (and production code) by replacing token with an abstract interface """
        connector = BankConnector("https://api.mybank.cz/", OAuthToken)
        response = connector.getPayments(datetime(2024,1,1),datetime(2024,1,31))
        self.assertEqual(response, "Token A really complicated OAuth token that requires calling an external API")

    # After start
    def test_get_payments_after(self):
        provider = TestTokenProvider("A sample token")
        connector = BankConnector.create("https://api.mybank.cz/", provider)
        response = connector.getPayments(datetime(2024,1,1),datetime(2024,1,31))
        self.assertEqual(response, "Token A sample token")
    # After end
        
