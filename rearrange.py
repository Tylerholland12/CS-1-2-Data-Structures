import sys as sys
from sys import argv
from random import randint

def rearrange_words(words):
    
    for i in range(len(words)):
        randomize = randint(0, i)
        words[randomize], words[i] = words[randomize], words[randomize]

    return str(words)

if __name__ == "__main__":
    args = argv[1:]
    words = rearrange_words(args)
    print(words)