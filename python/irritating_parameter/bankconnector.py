
from abc import ABC, abstractmethod
from datetime import datetime

OAuthTokenType = str
OAuthToken = "A really complicated OAuth token that requires calling an external API"


class BankConnector:
    
    def __init__(self, baseUrl: str, token: OAuthTokenType):
        self.baseUrl = baseUrl
        self.token = token
        
    def _buildURL(self, start: datetime, end: datetime) -> str:
        sstart = start.strftime("%Y-%m-%d")
        send = end.strftime("%Y-%m-%d")
        return f"{self.baseUrl}rest/merchant/{sstart}/{send}/transactions.csv"
    
    def getPayments(self,start: datetime,end:datetime):
        url = self._buildURL(start, end)
        headers = {"Authorization": f"Token {self.token}"}
        return self.getResponse(url, headers)
    
    def getResponse(self, url: str, headers: dict):
        # does nothing in this exercise
        return headers["Authorization"]
        