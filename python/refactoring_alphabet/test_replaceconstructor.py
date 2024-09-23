from os import path
import unittest

from refactoring_alphabet.replaceconstructor import Exporter


class CoordinateHelperTest(unittest.TestCase):
    def test_data_are_written_to_storage(self):
        exporter = Exporter()
        exporter.export(b"12345")
        self.assertEqual(path.getsize("export.csv"),5)
