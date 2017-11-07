""" PSIT Week 10
Wiput Pootong (60070090)
Day2011
"""

def main():
    """ Find day from calendar """

    week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    # Get input
    day = int(input())
    month = int(input())

    print(week[(sum(months[:month - 1]) + day - 1) % 7])

main()
