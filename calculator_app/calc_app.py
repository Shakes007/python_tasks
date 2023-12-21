# This program is designed to act as a calculator.
# It must take two numbers and do a calculation
# with one of the operators "+,-,/,*".

# Import the numpy module in order to do the operations more efficiently. 
import numpy as np


def add_num(a, b):
    '''Takes in two numbers, returns the sum of the two values.'''
    y = np.add(a, b)
    # If the file "equations" does not exist, create one,
    # then add to it all calculations that the user has made.
    with open('equations.txt', 'a') as file:
        file.write(f'{a} + {b} = {y}\n')
    return y


def subtract_num(a, b):
    '''Takes in two numbers, returns the result of a subtract b. '''
    y = np.subtract(a, b)
    with open('equations.txt', 'a') as file:
        file.write(f'{a} - {b} = {y}\n')
    return y


def multiply_num(a, b):
    '''Takes in two numbers, returns the product of the two values.'''
    y = np.multiply(a, b)
    with open('equations.txt', 'a') as file:
        file.write(f'{a} * {b} = {y}\n')
    return y


def divide_num(a, b):
    '''Takes in two numbers, returns the quotient of the two values.'''
    y = np.divide(a, b)
    with open('equations.txt', 'a') as file:
        file.write(f'{a} / {b} = {y}\n')
    return y


print('Welcome!')

# While loop to prompt the user to get information.
while True:
    menu = input('''
Would you like to perform a calculation or view previous calculations?
c  - Calculator
vp - View Previous
''').lower()

    print('')

    if menu == 'c':
        while True:
            # If the user selects Calculator, ask the user to enter two numbers.
            try:
                num_a = int(input('Enter your first number: '))
                num_b = int(input('Enter your second number: '))
                break
            # Should the user enter a letter or an empty space,
            # make an exception in the program to handle this.
            except ValueError:
                print('You have not entered an Integer.')
                print('Please try again.')
                print('')

        sub_menu = input('''Which type of calculation would you like to make?
a  -  Addition
d  -  Divison
s  -  Subtraction
m  -  Multiplication
-1 -  Exit
''').lower()
        
        # If the user selects Addition, calculate the sum of the two variables
        # and print out the calculation with the answer.
        if sub_menu == 'a':
            print(f'{num_a} + {num_b} = {add_num(num_a, num_b)}')
        
        # If the user selects Division, calculate the sum of the two variables
        # and print out the calculation with the answer.
        elif sub_menu == 'd':
            try:
                print(f'{num_a} / {num_b} = {divide_num(num_a, num_b)}')
            # If the user enters a number to be divided by 0,
            # print out a valid error message.
            except ZeroDivisionError:
                print('Invalid calculation, cannot divide by 0.')
        
        # If the user selects Subtraction, calculate the sum of
        # the two variables and print out the calculation with the answer.
        elif sub_menu == 's':
            print(f'{num_a} - {num_b} = {subtract_num(num_a, num_b)}')

        # If the user selects Multiplication, calculate the sum of
        #  the two variables and print out the calculation with the answer.
        elif sub_menu == 'm':
            print(f'{num_a} * {num_b} = {multiply_num(num_a, num_b)}')
        
        # If the user enters anything other than what is in the menu.
        # Print a valid error message.
        else:
            print('Input error, please try again.')

    # Display previous calculations to the user.
    elif menu == 'vp':
        try:
            with open('equations.txt', 'r') as file:
                lines = file.read()
                print(lines)
        # If the user has made no previous calculations,
        # print a valid error message.
        except FileNotFoundError:
            print('There are no previous calculations.')

    else:
        print('Error, inavlid input.')
        print('')
