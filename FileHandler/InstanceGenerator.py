import random
import os

class InstanceGenerator:
    def __init__(self, size, constrains = None):
        self.size = size
        if constrains == None:
            self.constrains = size * 1000
        else:
            self.constrains = constrains
        self.fileName = None

    def AssembleFileName(self):
        string = 'gen_size_'
        string += str(self.size)
        string += '_constrains_'
        string += str(self.constrains)
        string += '.txt'
        self.fileName = string

    def createPath(self):
        if not os.path.exists('IOFiles'):
            os.makedirs('IOFiles')
        try:
            self.pathName = 'IOFiles/' + self.fileName
        except TypeError:
            self.AssembleFileName()
            self.pathName = 'IOFiles/' + self.fileName

    def generate(self):
        if self.fileName == None:
            self.AssembleFileName()
        with open(self.fileName, 'w') as f:
            pass
