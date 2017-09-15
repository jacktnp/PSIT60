"""
Week 5
BootSequence
"""

def main():
    """ Main function """
    amount = int(input())
    for count in range(1, amount + 1):
        if count != amount:
            print(count, end="_")
            continue
        print(count)

main()
