""" PSIT Week 13
Wiput Pootong (60070090)
happyday
"""

def main():
    """ Calculate Happy day """

    happy = [int(x) for x in input().split(',')]

    happy_day = 0
    for count in range(len(happy)):
        condition = happy[count] >= 80
        condition += (happy[count] >= 20 and happy[count] - happy[count - 1] >= 10) and count != 0

        if condition:
            happy_day += 1

    print(happy_day)

main()
