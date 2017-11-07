""" PSIT Week 10
Wiput Pootong (60070090)
Missing Numbers
"""

def main():
    """ Print missing number """

    # Get input
    maximum = int(input())
    numbers = []
    while 1:
        number = int(input())
        if number == 0:
            break
        numbers.append(number)

    for count in range(1, maximum + 1):
        if count not in numbers:
            print(count)

main()
