from configparser import ConfigParser

class Configuration:
    @classmethod
    def get_value(cls, key: str) -> str:
        config = ConfigParser()
        config.read("env.conf")
        return config.get('Database', key)        
    
