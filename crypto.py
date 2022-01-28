# -----------------------------------------------------------------------------
# Name:        crypto
# Purpose:     CS 21 assignment # 3
#
# Author:      David Markowitz
# Date:        Jan 28, 2019
# -----------------------------------------------------------------------------
"""
Python program that encrypts or decrypts a given text into/from  a secret
language.

Individual words in the text are encrypted according to the following rules:

    If the word starts with a vowel append 'bin' to the word.  The vowels are
    a, e, i, o, u.
    Otherwise, take the first letter of the word, move it to the end and then
    append 'ar'.

So:

    apple becomes applebin
    orange becomes  orangebin
    banana becomes ananabar
    car becomes arcar

For simplicity we'll assume that the input text is in lowercase and that it
does not contain any punctuation (no commas, periods, etc...)

Your program will first ask the user to make a choice between encryption into
the secret language (E or e) or decryption from the secret language (D or d).

When the user specifies 'E' or 'e' for encryption, the program will translate
each word in the input text into the secret language, will put the translated
words in reverse order into one translated message and will print out the
translated message.  The translated message will have exactly one space
character between words.

When the user specifies 'D' or 'd' for decryption', the program will attempt
to recover the original words from the input text.  This is only possible if
the words have a specific format:  they start with a vowel and end with bin
or they end with a consonant followed by ar.  If one or more word does not
have this format, the decryption fails and the message 'Invalid message.'
is printed.
"""

def starts_with_vowel(word):
    """
    Function to check whether individual words begin with a vowel or consonant

    Parameters: 
        word (string)
    Returns:
        result (boolean) 
    """
    # return True if the word starts with a vowel and False otherwise
    if word[0] in ['a','e', 'i', 'o', 'u']:
        result = True
    else:
        result = False
    return result


def encrypt(word):
    """
    Function that encrypts a single word into a secret language.

    Parameters:
        word (string)
    Returns:
        result (string)
    """
    # encrypt a single word into the secret language
    # call starts_with_vowel to decide which pattern to follow
    # return a single word (encrypted)
    if starts_with_vowel(word):
        result = word + 'bin'
    else:
        result = word[1:]+word[:1]+'ar'
    return result

def decrypt(word):
    """
    Function that decrypts a single word from a secret language.

    Parameters:
        word (string)
    Returns:
        result (string)
    """
    # decrypt a single word from the secret language
    # if the word is not a valid word in the secret language, return None
    if len(word) > 2 \
           and ((starts_with_vowel(word) and word[-3:] == 'bin')  \
           or (word[-2:] == 'ar' and word[-3] not in ['a','e','i','o','u'])):
        if starts_with_vowel(word) and word[-3:] == 'bin':
            result = word[:-3]
        else:
            result = word[-3] + word[:-3]
    else:
        result = None
    return result

def translate(text, mode):
    """
    Function that encrypts or decrypts an entire message.

    Parameters:
        text (string), mode (string)
    Returns:
        result (string)
    """

    word_list = text.split()      # Split the text into a list of words
    altered_word_list = []        # list to hold encrypted/decrypted words

    if mode in ('e','E'):    # if mode is e or E encrypt each word in the list
        for word in word_list:
            encrypted_word = encrypt(word)
            altered_word_list.append(encrypted_word)
    elif mode in ('d','D'):  # if mode is d or D decrypt each word in the list
        for word in word_list:
            if not decrypt(word): # examine decrypt return value for each word.
                result = None     # if not a valid word, return None
                return result
            else:
                decrypted_word = decrypt(word)
                altered_word_list.append(decrypted_word)

    altered_word_list.reverse()          # Reverse the list
    result = ' '.join(altered_word_list) # Convert word list to a string
    return result

def choose_mode():
    """
    Function that prompts user for input repeatedly until they enter
    'E', 'e', 'D' or 'd'.

    Parameters:
        mode (string)
    Returns:
        result (string)
    """

    valid_input = False

    while not valid_input:               # prompt for mode input until valid
        mode = input("\nEnter 'E' to encrypt, 'D' to decrypt.  ")
        if mode in ('e','E','d','D'):
            valid_input = True           # update the boolean to exit the loop
        else:
            print("Print either 'E' to encrypt or 'D' to decrypt")
    return mode


def main():
    """Function that calls other functions until to perform translation

    Get the user choice 'E' or 'D' and save it in a variable.
    Prompt the user for the message to be translated.
    Translate the message by calling translate - save result.
    Print the result - or 'Invalid message.' if applicable.

    Parameters:
        none
    Returns:
        none
    """

    mode = choose_mode()
    text = input("Please enter a message: ") # prompt user for input text
    translation = translate(text, mode)
    if translation == None:
        print("\033[34mInvalid message.")
    else:
        print("\033[34mThe secret message is: ",translation)


    return


if __name__ == '__main__':
        main()
