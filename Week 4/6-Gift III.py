""" Week 4
Wiput Pootong (60070090)
"""

def main():
    """ Find the second place weight """
    amount = int(input())

    first = 0
    second = -1
    for count in range(amount):
        gift = float(input())
        if count == 0:
            first = gift
        else:
            if gift > first:
                second, first = first, gift
            elif gift < first and gift > second and gift >= 0:
                second = gift
    if amount < 2 or second == -1:
        print("Exit")
    else:
        print("%g" %second)

main()
