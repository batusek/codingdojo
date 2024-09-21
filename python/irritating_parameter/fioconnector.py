
from datetime import datetime


class FioConnector:
    def __init__(self, baseUrl: str, token: str):
        self.baseUrl = baseUrl
        self.token = token
        
    def _buildURL(self, start: datetime, end: datetime) -> str:
        sstart = start.strftime("%Y-%m-%d")
        send = end.strftime("%Y-%m-%d")
        return f"{self.URL_BASE}/rest/merchant/{self.token}/{sstart}/{send}/transactions.csv"
    
    # other methods would follow
        