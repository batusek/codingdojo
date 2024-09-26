export class DataFetcher {
    constructor(public country: string) {
        this.country = country;
    }
  
    async fetchData(indicator: string): Promise<any> {
      const apiUrl = `https://api.worldbank.org/v2/countries/${this.country}/indicators/${indicator}?per_page=100&format=json`;
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`Error fetching data: ${response.status}`);
        }
        return response.json();
      } catch (error) {
        throw error; // Re-throw the error for handling
      }
    }
  }
  
  export class DataProcessor {
    country: string;
    fetcher: DataFetcher;

    constructor() {
      // Complicated initialization can go here, resulting in country = "USA"
      this.country = "USA";
      this.fetcher = this.createFetcher(this.country); // Create fetcher during initialization
    }
  
    createFetcher(country: string): DataFetcher {
      return new DataFetcher(country);
    }
  
    async getGdpPerCapita(): Promise<number> {
      const data = await this.fetcher.fetchData("NY.GDP.PCAP.KD");
      return data[1][0].value;
    }
  
    setFetcher(fetcher: DataFetcher) {
        this.fetcher = fetcher
    }
  }