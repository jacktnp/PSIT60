""" PSIT Week 12
Wiput Pootong (60070090)
FoodGrade II
"""

def main():
    """ Calculate maximum chicken in the box """

    weight = int(input())

    chickens = input().split()

    chickens = sorted([int(x) for x in chickens])

    total = 0

    count = 0

    while 1:
        if count <= len(chickens) - 1:
            total += chickens[count]
            if total > weight:
                break
            count += 1
        else:
            break

    print(count)

main()
