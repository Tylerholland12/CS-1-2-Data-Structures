from random import randint
from sys import argv

"""Import the rearrange words function from the rearrange file
"""
from rearrange import rearrange_words

def dictonary_words(num_words):

    """Store the file with all of the words into a variable
    """
    # filename = "/usr/share/dict/words"
    filename = "/Users/tylerholland/documents/code/cs1.2/tweet-generator/source_text.txt"

    """open the file stored in the variable and
    """
    my_file = open(filename,"r") 

    """Read the lines in the variable
    """
    lines = my_file.readlines()

    word_histogram = {}

    for word in lines:

        word = word.rstrip()
        word_histogram[word] = word_histogram.get(word, 0) + 1

    print(word_histogram)

    """Close the file
    """
    my_file.close()
    # print(lines)

    """select a random set of words from the file and store in a data type
    """
    for line in range(num_words):
        randomize = randint(0, len(lines))
        
        print(lines[randomize])



if __name__ == "__main__":
    # print(sentence)
    args = argv[1]
    num_words = int(args)
    dictonary_words(num_words)
    print(num_words)
    print(args)