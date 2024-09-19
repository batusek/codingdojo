import os
import unittest

from invoiceitemmanager import InvoiceItemManager
from invoiceitemmanager import InvoiceItemManagerA

class TestInvoiceItemManager(InvoiceItemManagerA):
    def __init__(self):
        output = ""
        
    def save(self,line):
        self.output = line

class InvoiceItemManagerTest(unittest.TestCase):
    def test_calculation(self):
        manager = TestInvoiceItemManager()
        manager.save_item_total_amount(1,3,0.2)
        total = manager.output.split(";")[-1]
        self.assertAlmostEqual(float(total),3.6,2)
        
if __name__ == '__main__':
    unittest.main()        