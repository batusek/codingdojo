from configparser import ConfigParser
from typing import Self


    
class Configuration:
    # TODO: Turn to Singleton and possibility to set testing instance
    @classmethod
    def get_value(cls, key: str) -> str:
        config = ConfigParser()
        config.read("global_state/env.conf")
        return config.get('Database', key)        

# After start
class ConfigurationReadyToTest:
    @classmethod
    def instance(cls) -> Self:
        if not hasattr(cls,'_instance'):
            cls._instance = Configuration()
        return cls._instance
    
    @classmethod
    def set_instance(cls, instance: Self) -> None:
        cls._instance = instance

    def _get_value(self, key: str) -> str:
        config = ConfigParser()
        config.read("env.conf")
        return config.get("Database",key)
    
    @classmethod
    def get_value(cls, key: str) -> str:
        return cls.instance()._get_value(key)
# After end