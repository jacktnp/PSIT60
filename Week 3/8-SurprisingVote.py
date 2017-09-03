""" Week 3
Wiput Pootong (60070090)
"""

def main():
    """ Find that score is surprising or not """
    total = float(input())
    high = float(input())
    low = total - high * 2

    if low < 0:
        low = 0

    if high - low > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
