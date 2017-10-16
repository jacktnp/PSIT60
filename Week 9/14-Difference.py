""" PSIT Week 9
Wiput Pootong (60070090)
Difference
"""

def main():
    """ Display A - B in ascending list """

    # Initialize list to collect
    set_a = []
    set_b = []

    # Input how many numbers in set a and b
    count_a = int(input())
    count_b = int(input())

    # Get input for set a
    for _ in range(count_a):
        set_a.append(int(input()))

    # Get input for set b
    for _ in range(count_b):
        set_b.append(int(input()))

    # Loop number in serted set_a
    for number in sorted(set_a):
        # If number is not in set be it is A-B
        if number not in set_b:
            print(number, end=' ')

main()
