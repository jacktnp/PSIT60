""" PSIT Week 13
Wiput Pootong (60070090)
circularPrime
"""

def isprime(number):
    """ Find that number is prime or not """

    # 1 is not prime number
    if number == 1:
        return False

    # Try using 2 to number ** 0.5
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    # If nothing can divide number
    return True

def circular(number):
    """ Find that is circular or not """

    # If not prime no need to calculate
    if not isprime(number):
        return 0

    # Change number to string
    number_str = str(number)
    digits = len(number_str) - 1

    for _ in range(digits):
        # Move last digit to first
        number_str = number_str[-1] + number_str[:-1]
        # If it's not prime return 0
        if not isprime(int(number_str)):
            return 0

    # It's circular prime
    return number

def main():
    """ Find sum of curcular prime """
    number = int(input())

    result = [circular(x) for x in range(1, number + 1)]

    print(sum(result))

main()
