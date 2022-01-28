# -----------------------------------------------------------------------------
# Name:        aggregator.py
# Purpose:     CS 21A - implement a simple general purpose aggregator
#
# Author:      David Markowitz
# -----------------------------------------------------------------------------
"""
A simple general purpose aggregator program that systematically
compiles a specific type of information from multiple online sources.

The aggregator takes a filename and a topic as command line arguments.
The file contains a possibly very long list of online sources (urls).
The topic will be a string such as art, football, etc...
The aggregator will issue an error message if the command line arguments
provided are too few or too many.

The aggregator opens and reads the urls contained in the file, and reports
back on the subset of urls that contain a reference to the specified topic.

FROM 20.2...
To analyze or compile information found at a given url, we usually need to
look only at the content found outside the tags. That's what we'll do in our
aggregator assignment.

The program puts the output in a text file. That output contains both the urls
and the text containing the reference.
The output file is created in the working directory. Its name consists of the
topic followed by summary.txt. So when the topic is art, the output filename
will be artsummary.txt, when the topic is football, the output filename
will be footballsummary.txt.

Since our program is reading html documents and we are interested in actual
text (not in matches found inside html tags), the text containing the reference
will be delimited by the innermost angle brackets: >text containing the topic
to capture<. The angle brackets should not be included in the captured text.

Since our aggregator will be reading urls on the open web, it may encounter
errors: it can handle both URLError and DecodeError and generate the
appropriate message for each.

Usage: aggregator.py filename topic
filename: input  file that contains a list of the online sources (urls).
topic:  topic to be researched and reported on
"""

import urllib.request
import urllib.error
import re
import sys
import urllib.robotparser
import string


def get_urls(url_sources_list, topic):
    """
    Function that prompts the user for input until valid input is entered.

    Parameters:
        url_sources_list (file)
        topic (string)
    Returns:
        none
    """

    with open(url_sources_list, 'r', encoding='utf-8') as file:
        for url in file:
#            print('line 79: url in source file = ', url)
            try:
                with urllib.request.urlopen(url) as url_file:
                    decoded_url = url_file.read().decode('UTF-8')

            except urllib.error.URLError as url_err:
                print('Error opening url: ', url, url_err)
            except UnicodeDecodeError as decode_err:
                print('Error decoding url: ', url,'\n', decode_err)
            else:
                stripped_html_file = strip_html_tags(decoded_url)
                topic_search(stripped_html_file, topic, url)



def strip_html_tags(html_input):
    """
    strip html tags from an html file

    Parameters:
    html_input (file) - the input html file
    Return:
    scratch_flie (file) - output with html tags removed
    """

    stripped_html  = ''
    pattern = '\>.*?\<'       # extract text found outside angle brackets '< >'
    matches = re.findall(pattern, html_input, re.IGNORECASE | re.DOTALL)
    if matches:
        stripped_html = '\n'.join(matches)           # join with new line
    stripped_html = stripped_html.replace('<', '')   # strip angle brackets
    stripped_html = stripped_html.replace('>', '')
    scratch_file = 'stripped_html.txt'
    with open(scratch_file, 'w',
              encoding='utf-8') as my_file:
        my_file.write(stripped_html)
    return scratch_file

def topic_search(filename, topic, url):
    """
    search for topic keyword within an html file. Write to output summary file

    Parameters:
    filename (file) - the input stripped html file
    Return:
    output_file (file) - output file showing lines with located topic word
    """

    output_file = (topic + 'summary.txt')
    prev_match_in_url = False                 # check if topic found in url
    first_url_in_source_list = True
    with open(filename, 'r', encoding='utf-8') as file:
        prev_match_in_url = False  # check if topic found in url
        for line in file:
            line_lower = line.lower() #  convert the line to lower case
            for word in line_lower.split():  # then split it into words
                word = word.strip(string.punctuation)
                with open(output_file, 'a', encoding='utf-8') as out_file:
                    if word == topic:
                        if prev_match_in_url == False:
                            out_file.write('\n')
                            out_file.write('-' * 70)
                            out_file.write('\n')
                            out_file.write(url)
                            prev_match_in_url = True
                        out_file.write('\n')
                        out_file.write(line.strip())
                        break

    return output_file



def main():
    """
    This function calls other functions until an empty string is entered

    Parameters:
        none
    Returns:
        none
    """

    if len(sys.argv) != 3:  # Check for the right number of arguments
        print('Please try again: aggregator.py filename topic')
    else:
        try:
            topic = (sys.argv[2])  # Get the topic argument
        except ValueError:
            print('Please try again: aggregator.py filename topic')
        else:  # Print each entry in the sources file
            get_urls(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()