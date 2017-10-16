""" PSIT Week 9
Wiput Pootong (60070090)
Ascending
"""

def main():
    """ Sort 5 numbers ascending order """

    # Initialize numbers list
    numbers = []

    # Get 5 numbers and insert into list
    for _ in range(5):
        numbers.append(int(input()))

    # Print sorted numbers
    for number in sorted(numbers):
        print(number)

main()
