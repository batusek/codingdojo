import os
import unittest

from legacy_intro.legacyintro import *

class InvoiceItemManagerTest(unittest.TestCase):
    def setUp(self):
        super().setUp()
        try:
            os.remove("invoice_items.csv")
        except FileNotFoundError:
            pass
        
    def test_invoice_item_amount_calculated_correctly(self):
        manager = InvoiceItemManager()
        manager.save_item_total_amount(1,3,0.2)
        with open("invoice_items.csv","r") as f:
            text = f.read()
            
        total = float(text.split(";")[-1])
        self.assertAlmostEqual(total,3.6,2)

# After start
class InvoiceItemManagerATest(unittest.TestCase):
    def test_invoice_item_amount_calculated_correctly(self):
        manager = InvoiceItemManagerRefactored()
        self.assertAlmostEqual(manager.calculate_total(1,3,0.2),3.6,2)
# After end      