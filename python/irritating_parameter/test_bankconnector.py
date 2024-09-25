from datetime import datetime
import os
import unittest

from irritating_parameter.bankconnector import *



class BankConnectorTest(unittest.TestCase):
    def test_build_url(self):
        """ TODO: write a test that test the buildURL method by providing None for token """

    def test_get_payments(self):
        """ TODO: rewrite the test (and production code) by replacing token with an abstract interface """
        connector = BankConnector("https://api.mybank.cz/", OAuthToken)
        response = connector.getPayments(datetime(2024,1,1),datetime(2024,1,31))
        self.assertEqual(response, "Token A really complicated OAuth token that requires calling an external API")

        
