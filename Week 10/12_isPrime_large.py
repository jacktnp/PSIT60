""" PSIT Week 10
Wiput Pootong (60070090)
isPrime_large
"""

def isprime(number):
    """ Find that number is prime or not """

    # 1 is not prime number
    if number == 1:
        return "NO"

    # Try using 2 to number ** 0.5
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return "NO"

    # If nothing can divide number
    return "YES"

def main():
    """ Find prime large prime number """

    # Get input
    number = int(input())

    # Print output
    print(isprime(number))

main()
