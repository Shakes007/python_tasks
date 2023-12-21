def largest_number(numbers):
    '''
    Finds the largest number in a list of numbers.
    
    Parameters:
    - numbers (list): A list of numberic numbers.
    
    Returns:
    numberic or None: The largest number in the list, or None if the list
    is empty.
    
    If the list contains only one number, that number is returned.
    
    Example:
    >>> largest_number([3, 1, 7, 4, 5])
    7
    '''
    # If there are no numbers in the list, return nothing.
    if not numbers:
        return None

    # If there is only one number in the list, return it.
    if len(numbers) == 1:
        return numbers[0]

    # Find largest number in the list.
    rest_max = largest_number(numbers[1:])

    if numbers[0] > rest_max:
        return numbers[0]
    else:
        return rest_max
 

nums = [1, 5, 10]

# Call function.
result = largest_number(nums)
print(result)
