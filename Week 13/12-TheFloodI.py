""" PSIT Week 13
Wiput Pootong (60070090)
TheFlood I
"""

def main():
    """ Calculate maximum day can protect from flood """

    walls = [int(x) for x in input().split()]

    # Initialize day count
    days = 0

    while 0 not in walls:

        # Sorted walls strengh
        walls = sorted(walls)

        # Minus one of all walls except the weakest
        walls = [walls[0]] + [x - 1 for x in walls[1:]]

        # Count day
        days += 1

    # Print result
    print(days)

main()
