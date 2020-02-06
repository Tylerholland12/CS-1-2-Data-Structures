




def get_text_words(file):
    '''opens text file then puts it into an array of strings
    '''
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    words = []
    for line in lines:
        for word in line.split():
            words.append(word)
    return words

def histogram(text_file):
    ''' return a histogram data structure that stores each unique word along with the number of times the word appears in the source text
    '''
    histogram = dict()
    for word in text_file:
        print(word)
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram

def repeated_words(histogram):
    '''returns a list of repeated words
    '''
    list_repeated_words = []
    for word, count in histogram.items():
        if count > 1:
            list_repeated_words.append(word)
    return list_repeated_words

def unique_words(histogram):
    ''' returns the total count of unique words in the histogram
    '''
    return len(histogram)

def frequency(word, histogram):
    '''returns the number of times that a word appears in a text.
    '''
    return histogram[word]

if __name__ == '__main__':
    words = get_text_words('words.txt')
    histogram = histogram(words)
    print(repeated_words(histogram))
    # print(unique_words(histogram))
    print(frequency("of", histogram))