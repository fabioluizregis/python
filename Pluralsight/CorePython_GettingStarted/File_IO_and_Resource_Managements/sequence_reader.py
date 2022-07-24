"""Read and print an integer series"""
import sys

def read_series(filename):
    #with opens and close automatically at the end of reading
    with open(filename, mode='rt', encoding='utf-8')
    return [int(line.strip()) for line in f]


def main(filename):
    series = read_series(filename)
    print(series)