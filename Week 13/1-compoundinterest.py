""" PSIT Week 13
Wiput Pootong (60070090)
compoundinterest
"""

def main():
    """ Find result from interest rate """
    money = int(input())
    compound = float(input()) / 100
    time = int(input())

    for _ in range(time):
        money = money + (money * compound)

    print("%.2f" %money)

main()
