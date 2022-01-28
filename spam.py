# -----------------------------------------------------------------------------
# Name:        spam
# Purpose:     CS21A Assignment #4
#
# Author:      David Markowitz
# Date:        February 4, 2019
# -----------------------------------------------------------------------------
"""
A very simple spam classifier in Python.

This program will classify messages as either SPAM (unwanted) or HAM (wanted).
It will prompt the user for a message and then will print the corresponding
spam indicator with two decimal digits and the corresponding classification
(SPAM or HAM).

The program has a set of SPAM_WORDS, words that are known to appear in
spam messages.   

A spam threshold is defined which reflects the allowed percentage of
spam words in the message. A 'spam indicator' is calculated, which is the ratio
of spam words to the total number of unique words in the message.  If the spam
indicator exceeds the spam threshold, the message is classified as SPAM.
Otherwise it is classified as HAM.  The spam threshold is a constant and has a
value of 0.10. 

"""
import string                             # imports Python string methods

SPAM_WORDS = {'claim', 'congratulations', 'credit', 'dictator', 'discount',
              'expire', 'free', 'help', 'inheritance', 'lifetime', 'loan',
              'medicine', 'money', 'now', 'offer', 'opportunity', 'plan',
              'prize', 'rich', 'save', 'top', 'urgent', 'widow', 'winner'}

SPAM_THRESHOLD = 0.10                     # constant - spam id threshold

def spam_indicator(text):
    """
    Computes a 'spam indicator',  ratio of spam words / total unique words

    Parameters:
        text (string)
    Returns:
        indicator (float)
    """
    spam_count = 0
    words = text.split()                  # convert input string to a list
    word_set =set(words)                  # convert list to a set
    spam_set = word_set & SPAM_WORDS      # identify spam using intersection
    spam_count = len(spam_set)            # number of spam words in message
    total_words = len((word_set))         # total number of unique words
    indicator = spam_count / total_words  # compute ratio of spam / total words
    return indicator

def classify(indicator):
    """
    This function prints the spam classification

   Parameters:
        indicator (float)
    Returns:
        result (string)
     """
    f_indicator = f'{indicator:,.2f}'     # format output to 2 decimal places
    print("SPAM indicator = ", f_indicator)
    if indicator > SPAM_THRESHOLD:        # measure if % spam exceeds threshold
        result = 'SPAM'
    else:
        result = 'HAM'
    print("This message is: ", result)


def get_input():
    """
    Function that prompts the user for input until valid input is entered.

    Parameters:
        none
    Returns:
        text (string)
    """
    valid_input = False

    while not valid_input:                # prompt for input until valid
        text = input("Please enter your message. ")
        for char in string.punctuation:
            text = text.replace(char, '') # remove punctuation
        text = text.strip()               # remove white space (!div by 0)
        text = text.lower()               # convert text to lower case
        if text:
            valid_input = True            # update the boolean to exit the loop

    return text

def main():
    """Function that calls other functions to perform SPAM classification

        Get the user text message and save it in a variable.
        Prompt the user for the message to be classified - save result as text.
        Classify the message by calling  - save result as indicator.
        Print the result - or repeat prompt for input if applicable.

        Parameters:
            none
        Returns:
            none
    """
    # Get the user input and save it in a variable (as a string)
    # Call spam_indicator to compute the spam indicator and save it
    # Print the spam_indicator with two decimals
    # Call classify to print the classification

text = get_input()                        # call get_input function to get text
indicator = spam_indicator(text)          # call indicator function to measure
classify(indicator)                       # call classify function to id /print

if __name__ == '__main__':
    main()
