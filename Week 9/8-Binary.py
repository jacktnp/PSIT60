""" PSIT Week 9
Wiput Pootong (60070090)
Binary
"""

def main():
    """ Convert to binary """

    # Get decimal to convert to binary
    number = int(input())

    binary = ""

    # When input is 0
    if number == 0:
        binary = "0"

    # Divide until number is 0
    while number > 0:
        binary += str(number % 2)
        number //= 2

    # Print Result
    print(binary[::-1])

main()
