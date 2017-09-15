""" Sequence IV
Week 5 PSIT 2017 """

def main(num):
    """ Print 1 to n for n lines """
    for count in range(1, num ** 2 + 1):
        print(count, end=' ')
        if count % num == 0:
            print()

main(int(input()))
