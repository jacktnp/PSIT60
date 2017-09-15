""" Sequence IX
Week 5 PSIT 2017 """

def main(num):
    """ Print 1 to n for n lines """
    for count in range(-num + 1, 1):
        for _ in range(abs(count)):
            print(end='   ')
        for count2 in range(1, num - abs(count)):
            print("%02d" %count2, end=' ')
        for count2 in range(num - abs(count), 0, -1):
            print("%02d" %count2, end=' ')
        print()

main(int(input()))
