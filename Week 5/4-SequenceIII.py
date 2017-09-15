""" Sequence III
Week 5 PSIT 2017 """

def main(num):
    """ Print 2 to 2+n for n lines """
    for count in range(num):
        for i in range(count + 2, count + num + 2):
            print(i, end=' ')
        print()

main(int(input()))
