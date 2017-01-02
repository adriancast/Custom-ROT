#!/usr/bin/python
import string # To get abecedary
from utility import *


def main(argv):
    data = list(getDataFile())
    unCripted = []
    for item in data:
        letterUncripted = getUncriptedLetter(item,getRot())
        if letterUncripted != -1:
            unCripted.append(letterUncripted)
        else:
            unCripted.append(item)
    unCripted = ''.join(unCripted)
    print "Se ha descodificado como: ",unCripted
    pushDataFile(unCripted)


def getUncriptedLetter(letter,rot):
    ascii_letters = list(string.ascii_letters)
    idx = 0
    for abec_letter in ascii_letters:
        if letter == abec_letter:
            result = idx - rot
            while result > len(ascii_letters)-1:
                result = result % len(ascii_letters)
            return ascii_letters[result]
        idx = idx + 1
    return -1 #if is not in the ascii_letters



if __name__ == "__main__":
   main(sys.argv[1:])
