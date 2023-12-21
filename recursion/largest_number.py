def largest_number(numbers):
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
