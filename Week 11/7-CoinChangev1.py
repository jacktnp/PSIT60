""" PSIT Week 11
Wiput Pootong (60070090)
CoinChangev1
"""

def main():
    """ Main function """

    # Get input
    money = int(input())

    # Initialize result
    result = 0

    # Calculate 25 baht coin
    result += money // 25
    money %= 25

    # Calculate 10 baht coin
    result += money // 10
    money %= 10

    # Calculate 5 baht coin
    result += money // 5
    money %= 5

    # Remaining is 1 baht coin
    result += money

    print(result)

main()
