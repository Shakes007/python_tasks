# This program is designed to take input from a user.
# Enough numbers to form a list and
# calculate the integers in the list till a certain index.


# Function to check the value of the index at a given point and
# add it to the sum of the previous indexes.
def add_up_to(list, index):
    '''
    Calculates the sum of elements in a list up to a specified index.

    Parameters:
    - lst (list): A list of numeric values.
    - index (int): The index up to which the elements should be summed.

    Returns:
    numeric: The sum of elements in the list up to the specified index.

    Example:
    >>> add_up_to([1, 2, 3, 4, 5], 2)
    6

    The function recursively adds the current element (at the given index) to
    the sum of elements up to the previous index.

    Note: The index should be a valid index in the list; otherwise, an
    IndexError may occur.
    '''
    # Base case. Checks if index is 0 and returns the vallue at index 0.
    if index == 0:
        return list[0]
    else:
        # Add the current element(at the given index) to the sum
        # of elements up to the previous index.
        return list[index] + add_up_to(list, index - 1)


# Variable to store the users integers.
user_list = []

# While loop to request input from the user until user exits.
while True:
    numbers = int(input('Enter a list of numbers (Enter -1 to exit): '))

    # Checks if the user exits the program.
    if numbers == -1:
        break
    else:
        # If user does not exit, add the integers to the list that stores
        # the previous integers.
        user_list.append(numbers)

print('')
index = int(input('Enter an index you would like to stop at: '))
print('')

# Call function.
result = add_up_to(user_list, index)

print(f'Your list: {user_list}')
print('')
print(f'Your total at {index} is: {result}')
