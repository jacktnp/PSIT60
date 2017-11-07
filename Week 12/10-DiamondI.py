""" PSIT Week 12
Wiput Pootong (60070090)
Diamond I
"""

def main():
    """ Find the most diamond  """

    # How many set of diamond
    pack = int(input())
    # How many diamonds per set
    amount = int(input())

    result = [0 for _ in range(amount)]

    for _ in range(pack):
        diamond = input().split()
        for count in range(amount):
            result[count] += int(diamond[count])

    print(max(result))

main()
