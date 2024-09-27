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
    fetcher: DataFetcher;

    constructor() {
      // Complicated initialization can go here, resulting in country = "USA"
      let country = "USA";

      // create an object based on the previously constructed data
      // Uncomment: this.fetcher = new DataFetcher(country)
      // After start
      this.fetcher = this.createFetcher(country);
    }
  
    createFetcher(country: string): DataFetcher {
      return new DataFetcher(country);
    }
    // After end
  
    async getGdpPerCapita(): Promise<number> {
      const data = await this.fetcher.fetchData("NY.GDP.PCAP.KD");
      return data[1][0].value;
    }

    // After start
    setFetcher(fetcher: DataFetcher) {
        this.fetcher = fetcher
    }
    // After end
  }