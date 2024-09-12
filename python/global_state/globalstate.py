from configparser import ConfigParser
from typing import Self

class Configuration:
    @classmethod
    def instance(cls) -> Self:
        if not hasattr(cls,'_instance'):
            cls._instance = Configuration()
        return cls._instance

    def _get_value(self, key: str) -> str:
        config = ConfigParser()
        config.read("env.conf")
        return config.get('Database', key)        
    
    @classmethod
    def get_value(cls, key: str) -> str:
        return cls.instance()._get_value(key)
    
