import os
import unittest

from side_effect.invoiceitemmanager import *

class TestableInvoiceItemManager(InvoiceItemManagerA):
    def __init__(self):
        output = ""
        
    def save(self,line):
        self.output = line

class InvoiceItemManagerTest(unittest.TestCase):
    def test_calculation(self):
        manager = TestableInvoiceItemManager()
        manager.save_item_total_amount(1,3,0.2)
        total = manager.output.split(";")[-1]
        self.assertAlmostEqual(float(total),3.6,2)
        
