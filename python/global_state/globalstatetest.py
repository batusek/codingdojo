import unittest
from globalstate import Configuration


class GlobalStateTest(unittest.TestCase):
    def test_get_db_name(self):
        self.assertEqual(Configuration.get_value("DB_NAME"),"dev")

    def test_get_db_user(self):
        self.assertEqual(Configuration.get_value("DB_USER"),"developer")


if __name__ == '__main__':
    unittest.main()
