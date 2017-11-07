""" PSIT Week 11
Wiput Pootong (60070090)
FibonacciRecursionV2 (Refactored Version)
"""

def fibo(number, data):
    """ Return fibonacci values for given number """

    # If fibo is already in memory just return it
    if number in data:
        return data[number]

    # Minus 500 to prevent runtime error of python by find first under 500 position
    if number > 500:
        fibo(number - 500, data)

    # Find new fibo
    res = fibo(number-2, data) + fibo(number-1, data)

    # Add new fibo position
    data[number] = res

    # return result
    return res

print(fibo(int(input()), {0:0, 1:1}))
