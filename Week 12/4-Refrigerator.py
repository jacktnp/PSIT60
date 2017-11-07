""" PSIT Week 12
Wiput Pootong (60070090)
Refrigerator
"""

def main():
    """ Calculate maximum day can preserve food without losing """

    # Get how many food
    amount = int(input())

    # Get food expiry date
    food = input().split()

    # Convert food list to int
    food = [int(x) for x in food]

    # Initialize day count
    days = 0

    while 1:
        # Get lowest value index
        index = food.index(min(food))

        # When something has expired
        if min(food) == 0:
            break
        # Decrease expire date of foods which not in refrigerator
        for count in range(amount):
            if count != index:
                food[count] -= 1

        # Count day
        days += 1

    # Print result
    print(days)

main()
