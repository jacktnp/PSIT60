""" PSIT Week 8
Wiput Pootong (60070090)
PickThem
"""

import json

def main():
    """ Convert string into list with json.loads() then display only even numbers """

    # Input string and convert to list using json.loads()
    numbers = json.loads(input())

    # Initialize list to collect results
    result = []

    # Loop into numbers list select only even numbers add to result list
    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    # Print Nope if no result
    if len(result) == 0:
        print("Nope")
    # Print reverse result if has result
    else:
        for number in result:
            print(number)

main()
