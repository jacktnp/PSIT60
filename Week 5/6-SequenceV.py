""" Sequence V
Week 5 PSIT 2017 """

def main(num):
    """ Print 1 to n for n lines """
    for count in range(num, 0, -1):
        print(count, end=' ')
        if count % 7 == num % 7 + 1:
            print()

main(int(input()))
