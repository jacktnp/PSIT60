""" Sequence I
Week 5 PSIT 2017 """

def main(num):
    """ Print 1 to n for n lines """
    for _ in range(num):
        for i in range(1, num + 1):
            print(i, end=' ')
        print()

main(int(input()))
