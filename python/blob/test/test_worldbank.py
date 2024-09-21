import unittest

from blob.worldbank import DataProcessor
# After start
from blob.worldbank import DataFetcher

class TestDataProcessor(DataProcessor):
    def createFetcher(self, country: str):
        self.fetcher = DataFetcher("CZE")
# After end
    
class DataProcessorTest(unittest.TestCase):
    def test_getGdpPerCapita(self):
        # TODO: change this test to read data from Czech Republic
        processor = DataProcessor()
        gdp = processor.getGdpPerCapita()
        self.assertAlmostEqual(gdp, 65020, 0)

    # After start
    def test_getGdpPerCapitaCzechia_via_set_method(self):
        processor = DataProcessor()
        processor.setFetcher(DataFetcher("CZE"))
        gdp = processor.getGdpPerCapita()
        self.assertAlmostEqual(gdp, 19800, 0)

    def test_getGdpPerCapitaCzechia_via_subclass_and_override(self):
        processor = TestDataProcessor()
        gdp = processor.getGdpPerCapita()
        self.assertAlmostEqual(gdp, 19800, 0)
    # After end