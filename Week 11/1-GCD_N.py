""" PSIT Week 11
Wiput Pootong (60070090)
GCD_N
"""

def gcd(number1, number2):
    """ Find GCD of 2 numbers """
    # When reminder is 0
    if number2 == 0:
        return number1
    return gcd(number2, number1 % number2)

def main():
    """ Main function """
    count = int(input())

    numbers = []

    for _ in range(count):
        numbers.append(int(input()))
    if len(numbers) > 1:
        result = gcd(numbers[0], numbers[1])
    else:
        result = numbers[0]

    for count in range(2, len(numbers)):
        result = gcd(result, numbers[count])

    print(result)

main()
