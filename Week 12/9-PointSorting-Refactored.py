""" PSIT Week 12
Wiput Pootong (60070090)
Point Sorting (Refactored Version)
"""

def main():
    """ Sort coordinate """

    # Get number of datasets
    dataset = int(input())

    for _ in range(dataset):
        # Get number of dataset members
        member = int(input())

        # Got data and append to member
        coords = [[int(x) for x in input().split()] for _ in range(member)]

        # Sort data by sum then x coord decending you will get ascending y
        coords.sort(key=lambda x: (x[0] + x[1], x[0]))

        # Print result
        _ = [print(x, y) for x, y in coords]

main()
