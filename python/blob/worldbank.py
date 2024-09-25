import requests

class DataFetcher:
    def __init__(self, country: str):
        self.country = country
        
    def fetchData(self, indicator: str):
        api_url = f"https://api.worldbank.org/v2/countries/{self.country}/indicators/{indicator}?per_page=100&format=json"
        response = requests.get(api_url)
        if not response.status_code == 200:
            raise Exception(f"Error fetching data: {response.status_code}")
      
        return response.json()  
    
    
class DataProcessor:
    def __init__(self):
        # do some complicated init here that results in
        country = "USA"
        
        # create an object based on the previously constructed data
        self.fetcher = DataFetcher(country)
        
    def getGdpPerCapita(self) -> float:
        data = self.fetcher.fetchData("NY.GDP.PCAP.KD")
        return data[1][0]['value']
        
        
        