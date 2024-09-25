from configparser import ConfigParser
from typing import Self


    
class Configuration:
    # TODO: Turn to Singleton and possibility to set testing instance
    @classmethod
    def get_value(cls, key: str) -> str:
        config = ConfigParser()
        config.read("global_state/env.conf")
        return config.get('Database', key)        


