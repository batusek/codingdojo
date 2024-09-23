from configparser import ConfigParser
import unittest
from globalstate import Configuration


class TestableConfiguration(Configuration):
    def __init__(self):
        self.config = ConfigParser()
        
    def _get_value(self, key: str) -> str:
        return self.config.get("Database",key)

class ConfigurationTest(unittest.TestCase):
    def test_get_db_name(self):
        configuration = TestableConfiguration()
        configuration.config['Database'] = {
            'DB_NAME': 'internalDB',
            'DB_USER': 'internalUser'
        }
        Configuration.set_instance(configuration)
        self.assertEqual(Configuration.get_value("DB_NAME"),"internalDB")

    def test_get_db_user(self):
        configuration = TestableConfiguration()
        configuration.config['Database'] = {
            'DB_NAME': 'internalDB',
            'DB_USER': 'internalUser'
        }
        Configuration.set_instance(configuration)
        self.assertEqual(Configuration.get_value("DB_USER"),"internalUser")

