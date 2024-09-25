import unittest

from refactoring_alphabet.changemethodsignature import *


class CoordinateHelperTest(unittest.TestCase):
    def test_0_0_is_the_beginning_of_the_coordinate_system(self):
        self.assertEqual(CoordinateHelper.distance_from_beginning(0,0),0)
        
    def test_1_1_distance_is_equal_to_the_square_root_of_2(self):
        self.assertAlmostEqual(CoordinateHelper.distance_from_beginning(1,1),1.41,2)
        
# After start
class CoordinateHelperAfterTest(unittest.TestCase):
    def test_0_0_is_the_beginning_of_the_coordinate_system(self):
        self.assertEqual(CoordinateHelperAfter.distance_from_beginning(Point(0,0)),0)
        
    def test_1_1_distance_is_equal_to_the_square_root_of_2(self):
        self.assertAlmostEqual(CoordinateHelperAfter.distance_from_beginning(Point(1,1)),1.41,2)
# After end
