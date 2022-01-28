# -----------------------------------------------------------------------------
# Name:         tax
# Purpose:      a simple sales tax calculator.
#
# Author:       David Markowitz
# Date:         Jan 13, 2019
# -----------------------------------------------------------------------------
"""
CS 21A Assignment 1 - Tax Calculator

This is a Python3 program that prompts the user for the price of three items,
calculates the sum of the items, then computes the sales tax to be charged for
the sum and the total cost. It hen prints the results.

The sales tax rate is for San Francisco, CA.  In 2019 the tax rate is 9.25%.
This tax rate is used as a constant in the program.

Valid input:

Input is assumed to be valid - the price entered by the user is a valid
non-negative number.

Rounding:

Amounts are rounded to two decimal numbers.

Testing:

This program has been run and tested with multiple sets of numbers.
"""

prompt = ('Please enter the price for the first item in $: ')
amount_1 = float(input(prompt))   # user input to create variable 'amount_1'

prompt = ('Please enter the price for the second item in $: ')
amount_2 = float(input(prompt))   # user input to create variable 'amount_2'

prompt = ('Please enter the price for the third item in $: ')
amount_3 = float(input(prompt))   # user input to create variable 'amount_3'

TAX_RATE = 9.25 / 100                       # constant 'TAX-RATE'
sum = amount_1 + amount_2 + amount_3        # calculate sum
tax = sum * TAX_RATE                        # calculate tax
total = sum + tax                           # calculate total amount

# format output - round to 2 decimal places and remove space after $

sumf = f'${sum:,.2f}'            # Formatted string for sum prefixed with $ sign
taxf = f'${tax:,.2f}'            # Formatted string for tax prefixed with $ sign
totalf = f'${total:,.2f}'        # Formatted string for sum prefixed with $ sign

sumf_output = f'Purchase Amount:{sumf:>15}' # Sum output string - right aligned
taxf_output = f'Sales Tax:{taxf:>21}'       # Tax output string - right aligned
totalf_output = f'Total:{totalf:>25}'     # Total output string - right aligned

print(sumf_output)
print(taxf_output)
print(totalf_output)
