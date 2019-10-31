import os
from FileHandler.FileReader import FileReader
from TSPCoreComponents.Vertex import Vertex

def Main():
    scan = FileReader('test_instance.txt')
    x = scan.importInstance()
    print(x)

if __name__ == '__main__':
    Main()