import unittest
from yahtsee import Yahtsee, Category


class NumberTest(unittest.TestCase):
    def test_if_no_number_exists_score_is_zero(self):
        self.assertEquals(0,Yahtsee().score(Category.ONES,[2,3,2,4,5]))

if __name__ == '__main__':
    unittest.main()
