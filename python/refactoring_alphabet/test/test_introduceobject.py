from os import path
import unittest

from refactoring_alphabet.introduceobject import CostCalculator


class CostCalculatorTest(unittest.TestCase):
    def test_light_item_small_distance(self):
        calculator = CostCalculator()
        self.assertEqual(calculator.calculate_shipping_cost(8,3),5.3)        

    def test_light_item_large_distance(self):
        calculator = CostCalculator()
        self.assertEqual(calculator.calculate_shipping_cost(8,30),8)        
        
    def test_heavy_item_small_distance(self):
        calculator = CostCalculator()
        self.assertEqual(calculator.calculate_shipping_cost(15,3),10.3)        

    def test_heavy_item_large_distance(self):
        calculator = CostCalculator()
        self.assertEqual(calculator.calculate_shipping_cost(15,30),13)        
