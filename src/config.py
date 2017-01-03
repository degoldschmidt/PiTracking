# import the necessary packages
import configparser

class Configuration():
    def __init__(self):
        self.config = configparser.ConfigParser()

    def display(self):
        print("[","DEFAULT","]")
        for opts in self.config.defaults():
            print("\t", opts, ":", self.config.get("DEFAULT", opts))
        for sects in self.config.sections():
            print("[",sects,"]")
            for opts in self.config.options(sects):
                print("\t", opts, ":", self.config.get(sects, opts))

    def readFromFile(self, filename):
        self.config.read(filename)

    def write(self, _class="DEFAULT", _key="", _value=""):
        if isinstance(_key, str):
            self.config[_class] = {}
            self.config[_class][_key] = _value
        else:
            for ind, ekey in enumerate(_key):
                self.config[_class][ekey] = _value[ind]

    def writeToFile(self, filename):
        with open(filename, 'w') as configfile:
            self.config.write(configfile)

""" HOW TO USE
conf = Configuration()
conf.write(_key=['ServerAliveInterval', 'Compression', 'CompressionLevel'], _value=['45', 'yes', '9'])
conf.write('anything', 'User', 'hg')
conf.write('topsecret.server.com', 'Port', '45')
testfile = "../conf/test.ini"
conf.writeToFile(testfile)
conf.readFromFile(testfile)
conf.display()
"""
conf = Configuration()
conf.write(_key=['ServerAliveInterval', 'Compression', 'CompressionLevel'], _value=['45', 'yes', '9'])
