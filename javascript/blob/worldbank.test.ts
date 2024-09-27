// After start
import fetch from 'node-fetch'
// After end
import { expect, test } from 'vitest';
import { DataProcessor, DataFetcher } from './worldbank';

// After start
globalThis.fetch = fetch; // we use a default browser fetch for fetching
// After end


class TestDataProcessor extends DataProcessor {
  createFetcher(country: string): DataFetcher {
    return new DataFetcher("CZE");
  }
}

test('should get GDP per capita for Czech Republic', async () => {
    const processor = new DataProcessor();
    const gdp = await processor.getGdpPerCapita();
    expect(gdp).toBeCloseTo(65020, 0); // Adjust the expected value as needed
});

// After start
test('should get GDP per capita for Czech Republic via setFetcher method', async () => {
    const processor = new DataProcessor();
    processor.setFetcher(new DataFetcher("CZE"));
    const gdp = await processor.getGdpPerCapita();
    expect(gdp).toBeCloseTo(19800, 0); // Adjust the expected value as needed
});

test('should get GDP per capita for Czech Republic via subclass and override', async () => {
    const processor = new TestDataProcessor();
    const gdp = await processor.getGdpPerCapita();
    expect(gdp).toBeCloseTo(19800, 0); // Adjust the expected value as needed
});
// After end
