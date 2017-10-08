""" PSIT Week 8
Wiput Pootong (60070090)
AndAgain
"""
import json

def main():
    """ Sum of list member that one is odd one is even """

    # Initialize result list
    result = []

    # Use json.loads() to convert input into list
    list_1 = json.loads(input())
    list_2 = json.loads(input())

    # Calculate size of list to use in loop
    size = len(list_1)

    # Loop for n times (n is amount of members in list)
    for count in range(size):
        # If member of list 1 is odd and member is list 2 is even add to result
        if list_1[count] % 2 == 1 and list_2[count] % 2 == 0:
            result.append(list_1[count] + list_2[count])

    # No result
    if len(result) == 0:
        print("Nope")
    # Has result
    else:
        print(result)

main()
