# -----------------------------------------------------------------------------
# Name:    grader
# Purpose: CS 21A Assignment # 2
#
# Author:  David Markowitz
# Date:    January 19, 2019
# -----------------------------------------------------------------------------
"""
Python program that computes the letter grade earned in a fictional course.

The program will prompt the user to enter the grades earned on different
components of the course.  The program will keep prompting for grades until
the user types 'q'.

If 5 or more grades are entered, the lowest grade will be dropped.

The program then calculates the course average score assuming equal weights
(course average = sum of the grades / number of grades).

The course average is rounded to 1 decimal.  A letter grade will then be
assigned as determined by the following scale:
90 and above: A
80 - 89.9:  B
70 - 79.9: C
60 - 69.9: D
below 60: F 

In addition to the letter grade, the program prints the specific grade
that was dropped (when applicable), the rounded course average and the
remaining grades as shown in the expected output below.  The dropped grade
and the remaining grades are printed with two decimals.  The remaining grades
are aligned to the right.  """

# Enter your code here
# Use a constant for the minimum number of grades required for a drop
# Initialize a list for the grades to be entered by the user

MIN_GRADES = 5                  # min grades for lowest score to be dropped
grades = []                     # list of entered grades
stop_indicator = 'q'            # character that user may enter to end input
finished = False                # initialize a boolean variable

# Prompt the user for input repeatedly,
# adding each grade entered (as a number) to the grades list.
# Stop prompting when the user input is 'q'.

while not finished:
    user_input = input("Please enter a numeric grade. Press 'q' to quit. ")
    if user_input == 'q':
        finished = True         # update the boolean to exit the loop
    else:                       # check that user input is valid
        float_user_input = float(user_input)
        if float_user_input >= 0 and float_user_input <=100:
            grades.append(float_user_input)
        else:
            print("Please enter a grade between 0 and 100.")

# Are there enough grades to drop the lowest one?
# If so, remove and print the lowest grade with the correct formatting.

if len(grades) == 0:            # check that at least one grade was entered
    print("No grades entered.")
    exit()
elif len(grades) < MIN_GRADES:  # check if enough grades were entered to drop
    print("\nNot enough entries to drop the lowest grade.")

else:
    sorted_grades = grades[:]   # create a distinct copy using slice assignment
    sorted_grades.sort()        # perform sort on the copy
    dropped_grade = sorted_grades[0]
    print(f'The lowest grade dropped: {dropped_grade:>5.2f}')
    grades.remove(dropped_grade) # drop lowest grade from original list


# Use some list functions to compute and print the average numeric grade.
# The course average will first be rounded to 1 decimal.

overall_grade = round(sum(grades) / len(grades),1)
print("Course Average: " , overall_grade)


# Compute and print the letter grade.

if overall_grade >=90:
    letter_grade = 'A'
elif overall_grade >=80:
    letter_grade = 'B'
elif overall_grade >=70:
    letter_grade = 'C'
elif overall_grade >=60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print("Letter Grade: ",letter_grade)


# The dropped grade and the remaining grades must be printed with two decimals.
# The remaining grades must be aligned to the right.
# Loop through the grades list and print them with the correct formatting.

print("Based on the following grades:")
for value in grades:
    grade_output = f'{value:>6.2f}'
    print(grade_output)

