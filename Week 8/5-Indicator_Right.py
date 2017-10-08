""" PSIT Week 8
Wiput Pootong (60070090)
Indicator_Right
"""

def main():
    """ Print arrow with * """

    # column is how many * will print on each row
    column = int(input())
    # how many row will be print on (need to be odd for balance arrow)
    row = int(input())

    # Calculate maximum space by row // 2 to use with for loop
    space = row // 2

    # Count from -space to space and use absolute to prevent negative integer
    for count in range(-space, space + 1):
        # Calculate space count by space - |count| and * for column
        print(" " * (space - abs(count)), "*" * column, sep='')

main()
