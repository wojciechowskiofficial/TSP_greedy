import os

class FileReader:
    def __init__(self, fileName):
        self.fileName = fileName
        self.createPath()
        self.instance = list()

    def createPath(self):
        if not os.path.exists('IOFiles'):
            os.makedirs('IOFiles')
        self.filePath = 'IOFiles/' + self.fileName

    def importInstance(self):
        with open(self.filePath, 'r') as inFile:
            instanceSize = inFile.readline()
            for i in range(instanceSize):
                self.instance.append()
