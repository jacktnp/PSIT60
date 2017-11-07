""" PSIT Week 10
Wiput Pootong (60070090)
Perfect
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

def perfect(number):
    """ Calculate that is perfect number or not """
    perfects = []
    for count in range(2, number):
        if isprime(count):
            perfect_number = (2 ** (count - 1)) * ((2 ** count) - 1)
            if perfect_number > number:
                break
            elif perfect_number <= number and perfect_number not in perfects:
                perfects.append(perfect_number)
    return sum(perfects)



def main():
    """ Find number that is square free or not """

    # Get input
    number = int(input())

    print(perfect(number))

main()
