import unittest

from blob.worldbank import DataProcessor

class DataProcessorTest(unittest.TestCase):
    def test_getGdpPerCapita(self):
        # TODO: change this test to read data from Czech Republic
        processor = DataProcessor()
        gdp = processor.getGdpPerCapita()
        self.assertAlmostEqual(gdp, 65020, 0)

