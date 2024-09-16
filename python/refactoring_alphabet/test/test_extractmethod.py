import unittest

from refactoring_alphabet.extractmethod import Item, PriceCalculator


class PriceCalculatorTest(unittest.TestCase):
    def test_zero_list_means_zero_price(self):
        calculator = PriceCalculator(0.1)
        self.assertEqual(calculator.calculate_total_price([]),0)
        
    def test_a_taxable_item_uses_price_quanity_and_tax(self):
        item: Item = Item(price=4,quantity=2,is_taxable=True)
        calculator = PriceCalculator(0.1)
        self.assertEqual(calculator.calculate_total_price([item]),8.8)
        
    def test_a_non_taxable_item_ignores_tax(self):
        item: Item = Item(price=4,quantity=2,is_taxable=False)
        calculator = PriceCalculator(0.1)
        self.assertEqual(calculator.calculate_total_price([item]),8)

    def test_multiple_items_are_summed_non_taxable_item_ignores_tax(self):
        item1: Item = Item(price=4,quantity=2,is_taxable=False)
        item2: Item = Item(price=3,quantity=3,is_taxable=False)
        calculator = PriceCalculator(0.1)
        self.assertEqual(calculator.calculate_total_price([item1, item2]),17)

