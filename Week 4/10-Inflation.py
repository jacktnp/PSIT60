""" Inflation Week 4
Wiput Pootong (60070090)
"""

def main():
    """ Find future value """

    value = float(input())
    years = int(input())

    value *= 100
    value = int(value)

    for _ in range(years):
        value *= 10381
        value //= 10000

    decimal = value % 100
    value //= 100

    print("%01d.%02d" %(value, decimal))

main()
