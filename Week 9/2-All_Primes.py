""" PSIT Week 9
Wiput Pootong (60070090)
All_Primes
"""

def is_prime(number):
    """ Check from 1 to n/2 if can divide then it's not prime """

    # 1 is not prime number
    if number == 1:
        return False

    # Loop from 2 to number if any one before number can divide mean not prime number
    for count in range(2, number):
        if number % count == 0:
            return False

    # Return Yes when nothing can divide
    return True

def main():
    """ Count how many prime from 1 to n """

    # Get input to number
    number = int(input())

    # Result variable that get from is_prime function
    result = 0

    # Count how many prime in
    for count in range(1, number + 1):
        result += is_prime(count)

    # Print result
    print(result)

main()
