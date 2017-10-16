""" PSIT Week 9
Wiput Pootong (60070090)
isprime_small
"""

def is_prime(number):
    """ Check from 1 to n/2 if can divide then it's not prime """

    # 1 is not prime number
    if number == 1:
        return "No"

    # Loop from 2 to number if any one before number can divide mean not prime number
    for count in range(2, number):
        if number % count == 0:
            return "No"
    
    # Return Yes when nothing can divide
    return "Yes"

def main():
    """ Check input is prime or not? """

    # Get input to number
    number = int(input())

    # Result variable that get from is_prime function
    result = is_prime(number)

    # Print result
    print(result)

main()
