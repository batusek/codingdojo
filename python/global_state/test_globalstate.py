from configparser import ConfigParser
import unittest
from global_state.globalstate import *

class GlobalStateTest(unittest.TestCase):
    def test_get_db_name(self):
        self.assertEqual(Configuration.get_value("DB_NAME"),"dev")

    def test_get_db_user(self):
        self.assertEqual(Configuration.get_value("DB_USER"),"developer")



