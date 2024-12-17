from unittest import TestCase

from canonical_tdd.colors import ColorEvaluator

class ColorEvaluatorTest(TestCase):
    def test_nearest_color_of_red_is_red(self):
        self.assertEqual(ColorEvaluator("f00").nearest_color(),"f00")
        
    def test_nearest_color_of_green_is_green(self):
        self.assertEqual(ColorEvaluator("0f0").nearest_color(),"0f0")        
        
    def test_nearest_color_of_blue_is_blue(self):
        self.assertEqual(ColorEvaluator("00f").nearest_color(),"00f")                
        
    def test_nearest_color_of_near_red_is_red(self):
        self.assertEqual(ColorEvaluator("edc").nearest_color(),"f00")                        
        
    def test_nearest_color_of_near_green_is_green(self):
        self.assertEqual(ColorEvaluator("153").nearest_color(),"0f0")                                

    def test_nearest_color_of_near_blue_is_blue(self):
        self.assertEqual(ColorEvaluator("17d").nearest_color(),"00f")                                
        
    def test_nearest_color_of_far_red_is_red(self):
        self.assertEqual(ColorEvaluator("1dc").farthest_color(),"f00")                        
        
        