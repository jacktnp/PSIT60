""" Sequence XII
Week 5 PSIT 2017 """

def main(num):
    """ Print by pattern """
    for i in range(1-num, num):
        for j in range(1-num, num):
            print("%02d" %(num-abs(abs(j)-abs(i))), end=" ")
        print()

main(int(input()))
