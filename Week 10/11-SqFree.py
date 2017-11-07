""" PSIT Week 10
Wiput Pootong (60070090)
SqFree
"""

import math

def squarefree(number):
    """ Calculate that is square free or not """

    sqroot = round(math.sqrt(number))

    # In case number under 2 always SquareFree
    if number < 2:
        return True

    # In case squareroot of number then square is equal to number it's not square free
    if sqroot * sqroot == number:
        return False

    # In case square root is lower than 2
    if sqroot <= 2:
        return True

    # Count from 2 to square root then if number can divide by count square
    for count in range(2, sqroot):
        if number % (count * count) == 0:
            return False

    # Nothing can divide mean it's square free
    return True


def main():
    """ Find number that is square free or not """

    # Get input
    number = int(input())

    # Initialize count variable to 0
    sq_free = 0

    # Count 1 to number
    for count in range(1, number + 1):
        sq_free += squarefree(count)

    # Print result
    print(sq_free)


main()
