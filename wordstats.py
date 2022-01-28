# -----------------------------------------------------------------------------
# Name:        wordstats
# Purpose:     CS21A - Assignment 5
#
# Author:      David Markowitz
# Date:        February 10, 2019
# -----------------------------------------------------------------------------
"""
Python program that computes language statistics of an input file.

    The program prompts the user for the filename
    - Finds the longest word in the file (could be one of many the same length)
    - Finds the five most common words with the number of times they appear
    - Finds the word count of all the words in the file, sorted alphabetically

"""

import string
# The following imports are needed for the draw_cloud function.
import tkinter
import tkinter.font
import random

# The draw_cloud function is only needed for the optional part:
# to generate a word cloud.
# You don't need to change it.
def draw_cloud(input_count, min_length=0):
    """
    Generate a word cloud based on the input count dictionary specified.

    Parameters:
    input_count (dict): represents words and their corresponding counts.
    min_length (int):  optional - defaults to 0.
         minimum length of the words that will appear
         in the cloud representation.
    Only the 20 most common words (that satisfy the minimum length criteria)
    are included in the generated cloud.
    """
    root = tkinter.Tk()
    root.title("Word Cloud Fun")
    # filter the dictionary by word length
    filter_count = {
        word: input_count[word] for word in input_count
        if len(word) >= min_length}
    max_count = max(filter_count.values())
    ratio = 100 / max_count
    frame = tkinter.Frame(root)
    frame.grid()
    current_row = 0
    for word in sorted(filter_count, key=filter_count.get, reverse=True)[0:20]:
        color = '#' + str(hex(random.randint(256, 4095)))[2:]
        word_font = tkinter.font.Font(size=int(filter_count[word] * ratio))
        label = tkinter.Label(frame, text=word, font=word_font, fg=color)
        label.grid(row=current_row % 5, column=current_row // 5)
        current_row += 1
    root.mainloop()


# Enter your own helper function definitions here

# Write a function count_words that reads a given file, line by line,
# then word by word, and returns a dictionary.  The dictionary should have an
# entry for each word in the file. The value corresponding to a given word
# should be the number of times the word appears in the file.

# The dictionary will be of the form :

# {'the': 20, 'ate': 1, 'morning': 2, etc...}

# As you process a given word from a given line in the file you can check
# whether that word is already in the dictionary:  if it is,  update the count.
# Otherwise you create a new dictionary entry and initialize it.

def count_words(filename):
    """
    Reads a given file, line by line, word by word, and returns a dictionary

    Parameter:
        filename (string)
    Returns:
        word_dict (dictionary)
    """

    word_dict = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.lower() #  convert the line to lower case
            for word in line.split():  #  then split it into words
                # take out leading and trailing special characters
                word = word.strip(string.punctuation + string.digits)
                if word:   # if word is not an empty string
                    if word in word_dict:
                        word_dict[word] += 1  # increment the tally by one
                    else:
                        word_dict[word] = 1   # add the word to the dictionary
    return (word_dict)


# Use the sorted function on the dictionary to get the different sorts.
# For some, you'll need to specify the key argument.
# Take advantage of Python built-in function max.
# Take advantage of list slicing:  my_list[0:10] is the list of the first 10
# items in my_list.
# Make sure that you open the input file only once and read it one line at
# a time.


def report(word_dict):
    """
    Function that calls other functions to provide statistics for a text file

    Parameters:
        word_dict (dictionary)
    Returns:
        none
    """

    # report on various statistics based on the given word count dictionary

    long_word = (max(word_dict, key=len))
    print('\nThe longest word is: ', long_word)

    # Print the five most common words

    print('\nThe 5 most common words are: \n')

    word_list = sorted(word_dict, key=word_dict.get,reverse=True)
    top_five_words = (word_list[0:5])         # splice list to return top 5
    for (top_word) in top_five_words:
        word_tally = str(word_dict[top_word])
        output_top_words = f'{top_word}: {word_tally}'
        print(output_top_words)

    # Write sorted word count results to an output file 'out.txt'

    with open('out.txt', 'w', encoding='utf-8') as my_file:
        for word in sorted(word_dict, reverse=False):
            my_file.write(word + ': ' + str(word_dict[word]) + '\n')


def main():
    """
    This function calls other functions until an empty string is entered

    Parameters:
        none
    Returns:
        none
    """

    filename = input("Please enter a file name: ")
    word_dict = count_words(filename)
    report(word_dict)
#    draw_cloud(word_dict)


if __name__ == '__main__':
    main()