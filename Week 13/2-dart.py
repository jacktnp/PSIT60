""" PSIT Week 13
Wiput Pootong (60070090)
dart
"""

def score(posx, posy):
    """ Calculate dart point """
    distance = (posx ** 2 + posy ** 2) ** 0.5

    # 5 Point radius
    if distance <= 2:
        return 5

    # 4 Point radius
    if distance <= 4:
        return 4

    # 3 Point radius
    if distance <= 6:
        return 3

    # 2 Point radius
    if distance <= 8:
        return 2

    # 1 Point radius
    if distance <= 10:
        return 1

    # Not in target = 0 Point (Got F!)
    return 0

def main():
    """ Calculate total dart point """

    rounds = int(input())

    total = 0

    for _ in range(rounds):
        posx, posy = [int(x) for x in input().split()]
        total += score(posx, posy)

    print(total)

main()
