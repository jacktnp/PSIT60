""" Week 6 PSIT 2017
Divide3Or5 """

def main():
    """ Calculator sum of 1 to n that can divide 3 or 5 """

    result = 0
    number = int(input())

    for count in range(1, number + 1):
        if count % 3 == 0 or count % 5 == 0:
            result += count

    print(result)

main()
