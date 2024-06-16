from lib.fs import ReadJsonFile, WriteJsonFile


class Subscriber:
    def __init__(self, name, callback):
        self.Name = name
        self.Callback = callback
    
    def run():
        self.Callback()

class Config:
    def __init__(self, filename):
        self.Filename = filename
        self.Subscribers = [Subscriber("default", print("Config change..."))]
        self.Config = ""
        
    def addSubscriber(self, callback):
        self.Subscribers.append(callback)
        
    def writeConfig(self, data):
        print("writting config...")
        WriteJsonFile(self.Filename, data)
        # for sub in self.Subscribers:
        #    sub.run()
        
    def loadConfig(self):
        print("reading config...", self.Filename)
        self.Config = ReadJsonFile(self.Filename)
        
    def getConfig(self, prop):
        return self.Config.get(prop)