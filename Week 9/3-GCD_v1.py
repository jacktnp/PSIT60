""" PSIT Week 9
Wiput Pootong (60070090)
GCD_v1
"""

def gcd(number1, number2):
    """ Find GCD of two numbers using Euclidean method """

    # When reminder is 0
    if number2 == 0:
        return number1
    return gcd(number2, number1 % number2)

def main():
    """ Calculate and display GCD of two numbers """

    # Get input number1 and number2
    number1 = int(input())
    number2 = int(input())

    # Result variable that get from gcd function
    result = gcd(number1, number2)

    # Print result
    print(result)

main()
