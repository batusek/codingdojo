import os
import unittest

from legacyintro import InvoiceItemManager
from legacyintro import InvoiceItemManagerA

class InvoiceItemManagerTest(unittest.TestCase):
    def setUp(self):
        super().setUp()
        os.remove("invoice_items.csv")
        
    def test_invoice_item_amount_calculated_correctly(self):
        manager = InvoiceItemManager()
        manager.save_item_total_amount(1,3,0.2)
        with open("invoice_items.csv","r") as f:
            text = f.read()
            
        total = float(text.split(";")[-1])
        self.assertAlmostEqual(total,3.6,2)

class InvoiceItemManagerATest(unittest.TestCase):
    def test_invoice_item_amount_calculated_correctly(self):
        manager = InvoiceItemManagerA()
        self.assertAlmostEqual(manager.calculate_total(1,3,0.2),3.6,2)
        
        
if __name__ == '__main__':
    unittest.main()        