# -----------------------------------------------------------------------------
# Name:        language
# Purpose:     CS21A Assignment #7
#
# Author:      David Markowitz
# Date:        March 4, 2019
# -----------------------------------------------------------------------------
"""
A simple Python program that opens a specified file, reads it, and learns the
words used in it as well as some basic structure information as to how the
words are ordered in a sentence.

The learn function return a dictionary where each word is mapped to a list of
all the words that immediately follow it in the input file. The function will
strip words of leading and trailing punctuation and convert them to lowercase
before adding them to the dictionary. infinite random sentence generator
function, sentence_generator.

The generator function then generates nonsensical sentences of a given length,
loosely modelled after some specified text file.
"""

class IndexNumbers(object):
    """
    An iterator for positive integers

    Argument:
    limit (int): upper limit on the sequence
    """

    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        else:
            result = self.current
            self.current = self.current + 1
            return result

    def __iter__(self):
        return self

import string
import random


def learn(filename):
    """
    opens and reads a file and learns words and basic structure information.

    Parameter:
        filename (string)
    Returns:
        word_dict (dictionary)

    """
    word_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.lower()              #  convert the line to lower case
            for word in line.split():        #  then split it into words
                word = word.strip(string.punctuation)     # remove punctuation
                if word:
                    word_list.append(word)                # add word to list

    index = IndexNumbers(len(word_list))         # establish range of iterator

    word_dict = {}
    for word in word_list:
        if word:
            i = next(index)                   # call iterator
            if i+1 < len(word_list):          # ensure index in range of list
                next_word = word_list[i + 1]
            else:
                next_word = ''                # create placeholder if last word

            if not word in word_dict and next_word == '':
                word_dict[word] = []          # create empty list for last word
                continue

            if not word in word_dict:
                    word_dict[word] = [next_word]  # add word and next to dict
            else:
                    word_dict[word] = word_dict[word] + [next_word] # next word
    return (word_dict)


def sentence_generator(filename, length=8):
    """
    makes up random sentences based on a dictionary

    Parameters:
        filename (string)
        length (integer)
    Yields:
        one random sentence at a time an infinite number of times
    """
    random.seed(100)  # Set the seed for the random generator - do not remove

    word_dict = learn(filename)
    all_keys = list(word_dict)                # list of keywords in dictionary
    while True:                               # infinite sentence generator
        added_words = []                      # create empty list for words

        new_word = random.choice(all_keys)    # random keyword selection
        added_words.append(new_word)          # add word to list of words

        while len(added_words) < length:      # add specified number of words
            follower_word_list = word_dict.get(new_word) # list keyword values
            if follower_word_list:            # verify keyword's values exist
                new_word = random.choice(follower_word_list) # pick random word
            else:
                new_word = random.choice(all_keys)  # random keyword selection
            added_words.append(new_word)       # add word to list of words

        random_sentence = (' ').join(added_words)   # join words with separator
        yield random_sentence                       # yield one random sentence