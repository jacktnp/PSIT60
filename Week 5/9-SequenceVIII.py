""" Sequence VIII
Week 5 PSIT 2017 """

def main(num):
    """ Print 1 to n triangle """
    for count in range(1, num + 1):
        for _ in range(num - count):
            print(end='   ')
        for count2 in range(1, count + 1):
            print("%02d " %count2, end='')
        print()
main(int(input()))
