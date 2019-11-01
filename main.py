from FileHandler.FileReader import FileReader
from TSPGreedy.Greedy import Greedy
from TSPGreedy.SolutionContainer import SolutionContainer

def Main():
    scan = FileReader('test_instance.txt')
    x = scan.importInstance()
    greed = Greedy(x)
    greed.solveGreedy()
    print(greed.solution)

if __name__ == '__main__':
    Main()