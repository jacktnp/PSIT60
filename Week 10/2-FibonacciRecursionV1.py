""" PSIT Week 10
Wiput Pootong (60070090)
FibonacciRecursionV1
"""

def fibo(num):
    """ Calculate fibo """
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibo(num - 1) + fibo(num - 2)

def main():
    """ Calculate fibo result """

    number = int(input())

    print(fibo(number))

main()
