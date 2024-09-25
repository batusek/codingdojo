class CloudStorage:
    def __init__(self, name: str):
        # initialize a cloud resource, simulated by a file here
        self.name = name
        
    def write(self, data: bytes) -> None:
        # store data in cloud, an expensive operation
        f = open(self.name,"wb")
        f.write(data)
        f.close()
       
        
class Exporter:
    def __init__(self):
        # TODO: replace a direct constructor call with a factory call 
        self.storage = CloudStorage("export.csv")
        
    def export(self, data: bytes):
        self.storage.write(data)

# After start
class StorageFactory:
    def createStorage(self, name:str):
        return CloudStorage(name)
        
class ExporterwithFatoryCall:
    def __init__(self):
        self.storage = StorageFactory().createStorage("export.csv")
        
    def export(self, data: bytes):
        self.storage.write(data)
# After end
