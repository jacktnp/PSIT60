""" PSIT Week 8
Wiput Pootong (60070090)
Hamburger
"""

def main():
    """ Print hamburger by | is bread and * is meats """

    # Get left and right bread count
    left_bread = int(input())
    right_bread = int(input())

    # Calculate meats by one bread can handle 2 slices of meats
    meat = (left_bread + right_bread) * 2

    # Print hamburger by | is bread and * is meat
    print("|" * left_bread, "*" * meat, "|" * right_bread, sep='')

main()
