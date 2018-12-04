import numpy as np
import nltk
import data_cleaner
import re
import random
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
from keras.models import Model
from keras.layers import Input, LSTM, Dense

max_sentence_length = 25
col_names = {'line':0, 'char':1, 'movie':2, 'name':3, 'dialogue':4}

def setup():
    """
    Initial setup. Cleans the training data and downloads NLTK tools.
    """
    data = data_cleaner.clean('movie_lines.tsv')
    nltk.download('punkt')
    nltk.download('wordnet')

def read_clean_data(file_name):
    """
    Reads in a cleaned dialogue text file and puts it in list of lists format.
    """
    file = open(file_name, encoding='utf-8', errors='ignore')
    rows = file.read().split('\n')
    rows.pop()
    lines = []
    for row in rows:
        row = row.split('\t')
        for col in range(0, 3):
            row[col] = int(row[col])
        lines.append(row)
    return lines

def create_sentence_pairs(data):
    print("Creating sentence pairs...")
    pairs = []
    pos = 0
    while pos < len(data):
        pos, convo = next_convo(pos, data)
        for i in range(len(convo) - 1):
            j = col_names['dialogue']
            pairs.append([convo[i][j], convo[i + 1][j]])

    print("Writing sentence pairs to txt file...")
    f = open('sentence_pairs.txt', 'w', encoding='utf-8', errors='ignore')
    s = ""
    for i in range(len(pairs)):
        if i % 2500 == 0:
            print("%d percent complete..." % (i * 100 / len(pairs)))
        pair = pairs[i]
        s += "{0}\t{1}\n".format(pair[0], pair[1])
    f.write(s)
    print("Sentence pairs file created.")
    return pairs

def read_sentence_pairs(file_name):
    """ Read back a list of input-target sentence pairs from a file. """

def next_convo(start, lines):
    """
    Returns a list of continuous dialogue turns, starting at START.
    :param lines - parsed and cleaned dialogue lines, a list of lists
    :param start - start index of the conversation, an int
    """
    i = start
    j = col_names['line']
    while i < len(lines) - 1 and lines[i + 1][j] == lines[i][j] + 1:
        i += 1
    return i + 1, lines[start:i + 1]

def train():
    """
    Prepares data for training the model.
    """
    input_data = Input(shape=(None,))
    data = read_clean_data('cleaned_lines.txt')

data = read_clean_data("cleaned_lines.txt")
pairs = create_sentence_pairs(data)
