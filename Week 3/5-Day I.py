""" Week 3
Wiput Pootong (60070090)
"""

def main():
    """ Find leap year or not """
    year = int(input())

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("Yes")
    else:
        print("No")

main()
