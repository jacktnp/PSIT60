""" Sequence XI
Week 5 PSIT 2017 """

def main(num):
    """ Print by pattern """
    for i in range(1, num*2):
        for j in range(1, num*2):
            print("%02d" %min(j-max(j-num, 0) * 2, i-max(i-num, 0) * 2), end=" ")
        print()

main(int(input()))
