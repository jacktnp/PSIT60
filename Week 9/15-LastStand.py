""" PSIT Week 9
Wiput Pootong (60070090)
LastStand
"""

import json

def main():
    """ Display last digit of numbers """

    # Get list of number in string format and use json.loads to convert list
    numbers = json.loads(input())

    # Get every member of numbers as number
    for number in numbers:
        # Because of integer to get first number you can use mod 10 to solve this
        print(number % 10)

main()
