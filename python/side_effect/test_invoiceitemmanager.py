import os
import unittest

from side_effect.invoiceitemmanager import *

class InvoiceItemManagerTest(unittest.TestCase):
    def test_calculation(self):
        # TODO: Rewrite the test (and the production code) so that it doesn't create a file at the test run
        manager = InvoiceItemManager()
        manager.save_item_total_amount(1,3,0.2)
        with open("invoice_items.csv", "r") as f:
            output = f.read()
            
        total = output.split(";")[-1]
        self.assertAlmostEqual(float(total),3.6,2)

# After start
class TestableInvoiceItemManager(InvoiceItemManagerWithIsolatedSideEffect):
    def __init__(self):
        output = ""
        
    def save(self,line):
        self.output = line

class TestableInvoiceItemManagerTest(unittest.TestCase):
    def test_calculation(self):
        manager = TestableInvoiceItemManager()
        manager.save_item_total_amount(1,3,0.2)
        total = manager.output.split(";")[-1]
        self.assertAlmostEqual(float(total),3.6,2)        
# After end
