#!/usr/bin/python
import string # To get abecedary
from utility import *


def main(argv):
    data = list(getDataFile())
    cripted = []
    for item in data:
        letterCripted = getCriptedLetter(item,getRot())
        if letterCripted != -1:
            cripted.append(letterCripted)
        else:
            cripted.append(item)
    cripted = ''.join(cripted)
    print "Se ha codificado como: ",cripted
    pushDataFile(cripted)

def getCriptedLetter(letter,rot):
    ascii_letters = list(string.ascii_letters)
    idx = 0
    for abec_letter in ascii_letters:
        if letter == abec_letter:
            result = idx + rot
            while result > len(ascii_letters)-1:
                result = result % len(ascii_letters)
            return ascii_letters[result]
        idx = idx + 1
    return -1 #if is not in the ascii_letters

if __name__ == "__main__":
   main(sys.argv[1:])
