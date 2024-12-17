from unittest import TestCase

from canonical_tdd.colors import ColorEvaluator

class ColorEvaluatorTest(TestCase):
    def test_nearest_color_of_red_is_red(self):
        self.assertEqual(ColorEvaluator("f00").nearestColor(),"f00")
        
    def test_nearest_color_of_green_is_green(self):
        self.assertEqual(ColorEvaluator("0f0").nearestColor(),"0f0")        
        
    def test_nearest_color_of_blue_is_blue(self):
        self.assertEqual(ColorEvaluator("00f").nearestColor(),"00f")                