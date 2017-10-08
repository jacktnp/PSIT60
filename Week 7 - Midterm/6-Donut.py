""" PSIT Week 7 (Midterm)
Wiput Pootong (60070090)
Donut
"""

def main():
    """ Calculate the lowest price with highest donuts """

    # Get input data
    price = int(input())
    base = int(input())
    free = int(input())
    demand = int(input())

    # Donuts per pack
    pack = base + free

    # How many packs will get
    packs = demand // pack

    # Calculate remain that not completed pack
    remains = demand % pack

    # Initialize donuts count with 0
    donuts = 0

    # Initialize cost with 0
    cost = 0

    # Remain is more or equal to base got 1 pack
    if remains >= base:
        packs += 1
    # If not got one pack calculate price of remain and add to dounts count
    else:
        donuts += remains
        cost += (remains * price)

    # Calculate how many donuts will get and add to donuts count
    donuts += (pack * packs)

    # Calculate cost that need to pay for donuts
    cost += (packs * base * price)

    # Print the result
    print("%d %d" %(cost, donuts))

main()
