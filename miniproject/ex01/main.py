from checkmate import *
from os.path import isfile, join
import sys

def main():
    argv = sys.argv 
    argv.pop(0)
    argc = len(argv)
    if argc > 0: 
        for board in argv:
            path = join("boards", board)
            if isfile(path):
                with open(path) as file:
                    checkmate(file.read())
            else:
                print("Error")

if __name__ == "__main__":
    main()