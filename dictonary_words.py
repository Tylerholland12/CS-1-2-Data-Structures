from random import randint

"Import the rearrange words function from the rearrange file"
from rearrange import rearrange_words

"Store the file with all of the words into a variable"
filename = "/usr/share/dict/words"

"open the file stored in the variable and"
my_file = open(filename,"r")

"Read the lines in the variable"
lines = my_file.readlines()

"Close the file"
my_file.close()
print(lines)


"select a random set of words from the file and store in a data type"


"put the number of words requested together into a sentence"


"output your sentence"