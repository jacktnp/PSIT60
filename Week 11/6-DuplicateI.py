""" PSIT Week 11
Wiput Pootong (60070090)
Duplicate I
"""

def main():
    """ Main function """

    # Get input
    group_a_count = int(input())
    group_b_count = int(input())

    # Initialize variable for collect data
    group_a = []
    group_b = []

    # Get Group A data
    for _ in range(group_a_count):
        group_a.append(int(input()))

    # Get Group B data
    for _ in range(group_b_count):
        group_b.append(int(input()))

    # Result list
    result = []

    # Find duplicate
    for number in group_a:
        if number in group_b:
            result.append(number)

    # No result print Nope
    if len(result) == 0:
        print("Nope")
    # If has result print decending result
    else:
        for number in sorted(result, reverse=True):
            print(number)

main()
