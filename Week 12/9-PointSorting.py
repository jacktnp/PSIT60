""" PSIT Week 12
Wiput Pootong (60070090)
Point Sorting
"""

def main():
    """ Sort coordinate """

    for _ in range(int(input())):
        amount = int(input())
        result = {}
        for _ in range(amount):
            posx, posy = input().split()
            posx, posy = int(posx), int(posy)
            total = posx + posy
            if total not in result:
                result[total] = []
            result[total].append([posx, posy])
        for index in sorted(result):
            for coord in sorted(result[index], key=lambda x: x[1], reverse=True):
                print(coord[0], coord[1])

main()
