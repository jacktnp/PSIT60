""" PSIT Week 11
Wiput Pootong (60070090)
Flatten
"""

import json

def flatten(numbers):
    """ Make nested list flatten """
    # Use isinstance() to verify list inside numbers
    if isinstance(numbers, list):
        # If it is blank list
        if len(numbers) == 0:
            return []
        # Flat first member of list and rest of list
        first, rest = numbers[0], numbers[1:]
        return flatten(first) + flatten(rest)
    else:
        # When all of members in numbers is flatten return list of numbe
        return [numbers]

def main():
    """ Main function """

    # Get input and convert to list
    numbers = json.loads(input())

    # Calculate result
    result = sorted(flatten(numbers), reverse=True)

    # Print result
    print(result)

main()
