# -----------------------------------------------------------------------------
# Name:        helloagain
# Purpose:     demonstrate command line arguments
#
# Author:      Rula Khayrallah
#
# -----------------------------------------------------------------------------
"""
print a customized hello a given number of times

usage: helloagain.py name number
"""
import sys

def main():
    print ('This is sys.argv:', sys.argv) # for demonstration purposes

    if len(sys.argv) != 3:  # Check for the right number of arguments
        print ('Please try again: helloagain.py name number')
    else:
        name = sys.argv[1]  # Get the name argument
        try:
            number = int(sys.argv[2])  # Get the number argument
        except ValueError:
            print ('Please try again: helloagain.py name number')

        else:   # Print the name the specified number of times
            for i in range (number):
                print ('Hello', name)

if __name__ == '__main__':
    main()