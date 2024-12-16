import fetch from 'node-fetch'
import { expect, test } from 'vitest';
import { DataProcessor, DataFetcher } from './worldbank';

globalThis.fetch = fetch; // we use a default browser fetch for fetching



test('should get GDP per capita for Czech Republic', async () => {
    const processor = new DataProcessor();
    const gdp = await processor.getGdpPerCapita();
    expect(gdp).toBeCloseTo(65020, 0); // Adjust the expected value as needed
});

