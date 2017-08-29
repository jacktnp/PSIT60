""" Pair Programming
Wiput Pootong (60070090)
Siwakorn Lertamnuaylap (60070095)
"""

def main():
    """ Calculate high of 8 numbers """

    high = find_high(input(), input())
    high = find_high(high, input())
    high = find_high(high, input())
    high = find_high(high, input())
    high = find_high(high, input())
    high = find_high(high, input())
    high = find_high(high, input())

    print(high)

def find_high(num1, num2):
    """ Find the highest of 2 value """
    num1, num2 = int(num1), int(num2)
    if num1 > num2:
        return num1
    return num2

main()
