""" Sequence VI
Week 5 PSIT 2017 """

def main(num):
    """ Print 1 to n for n lines """
    for count in range(1, num + 1):
        for count2 in range(1, count + 1):
            print(count2, end=' ')
        print()

main(int(input()))
