from unittest import TestCase

from canonical_tdd.colors import ColorEvaluator

class ColorEvaluatorTest(TestCase):
    def test_nearest_color_of_red_is_red(self):
        self.assertEqual(ColorEvaluator("f00").nearestColor(),"f00")