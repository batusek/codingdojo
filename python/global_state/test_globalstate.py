from configparser import ConfigParser
import unittest
from global_state.globalstate import *

class GlobalStateTest(unittest.TestCase):
    def test_get_db_name(self):
        self.assertEqual(Configuration.get_value("DB_NAME"),"dev")

    def test_get_db_user(self):
        self.assertEqual(Configuration.get_value("DB_USER"),"developer")



# After start
class TestableConfiguration(ConfigurationReadyToTest):
    def __init__(self):
        self.config = ConfigParser()
        
    def _get_value(self, key: str) -> str:
        return self.config.get("Database",key)

class ConfigurationTestWithInstance(unittest.TestCase):
    def test_get_db_name(self):
        configuration = TestableConfiguration()
        configuration.config['Database'] = {
            'DB_NAME': 'internalDB',
            'DB_USER': 'internalUser'
        }
        ConfigurationReadyToTest.set_instance(configuration)
        self.assertEqual(ConfigurationReadyToTest.get_value("DB_NAME"),"internalDB")

    def test_get_db_user(self):
        configuration = TestableConfiguration()
        configuration.config['Database'] = {
            'DB_NAME': 'internalDB',
            'DB_USER': 'internalUser'
        }
        ConfigurationReadyToTest.set_instance(configuration)
        self.assertEqual(ConfigurationReadyToTest.get_value("DB_USER"),"internalUser")
# After end