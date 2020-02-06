from flask import Flask
from histogram import histogram, frequency, unique_words
from sample import weighted_sample


app = Flask(__name__)


@app.route('/')
def generate_words():
    # return "this is the where the histogram function goes"

    '''build a histagram'''
    filename = open("./words.txt", "r")
    text_file = filename.readlines()
    # print(text_file)
    my_histogram = histogram(filename)

    # print(my_histogram)

    sentence = ''
    num_words = 10
    for i in range(num_words):
        word = weighted_sample(my_histogram)
        sentence += '' + word
    return sentence 


    # return my_histogram
    word = weighted_sample(my_histogram)
    return word

if __name__ == '__main__':
    app.run(debug=True)