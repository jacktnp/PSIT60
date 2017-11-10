""" PSIT Week 13
Wiput Pootong (60070090)
scaledmatrix
"""

def scale(number, mininum, difference):
    """ Calculate scale """
    return round(abs(number - mininum) / difference, 2)

def main():
    """ Make scaled matrix """

    row = int(input())
    col = int(input())
    matrix = [[float(input()) for _ in range(col)] for _ in range(row)]
    maximum = max([max(x) for x in matrix])
    minimum = min([min(x) for x in matrix])
    difference = abs(maximum - minimum)

    scaled = [[scale(y, minimum, difference) for y in x] for x in matrix]

    for row in scaled:
        for col in row:
            print("%.02f " %col, end='')
        print()

main()
