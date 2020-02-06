from histogram import histogram
from random import randint


def weighted_sample(histogram):
    tokens = sum([count for word, count in histogram])
    dart = random.randint(1, tokens)
    fence = 0

    for word, count in histogram:
        fence += count 
        if fence >= dart:
            return word


if __name__ == '__main__':
    print(weighted_sample(histogram))