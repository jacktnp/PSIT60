""" PSIT Week 8
Wiput Pootong (60070090)
PickThemAgain
"""

def main():
    """ Display member in list that can divide by 3 or 5 """

    # Get numbers convert to string then reverse
    numbers = input().split()

    # Initialize result list to collect results
    result = []

    # Convert all member in list into int
    numbers = [int(x) for x in numbers]

    # Loop members in numbers
    for number in numbers:
        # Print number that can divide by 3 or 5
        if number % 3 == 0 or number % 5 == 0:
            result.append(number)

    # Print Nope if no result
    if len(result) == 0:
        print("Nope")
    # Print reverse result if has result
    else:
        for number in reversed(result):
            print(number)

main()
