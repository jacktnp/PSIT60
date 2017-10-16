""" PSIT Week 9
Wiput Pootong (60070090)
Fibonacci_v3
"""

def main():
    """ Calculate Fibonacci n """

    # Get how many fibonacci we want
    number = int(input())

    # Initialize fibonacci
    position1, position2 = 0, 1

    # Loop to number - 1
    for _ in range(number):
        position1, position2 = position2, position1 + position2

    # Print Result
    print(position1)

main()
