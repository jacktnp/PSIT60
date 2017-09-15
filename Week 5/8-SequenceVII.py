""" Sequence VII
Week 5 PSIT 2017 """

def main(num):
    """ Print 1 to n for n lines """
    for count in range(-num + 1, num):
        for count2 in range(1, num - abs(count) + 1):
            print(count2, end=' ')
        print()

main(int(input()))
