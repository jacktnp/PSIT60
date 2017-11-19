""" PSIT Week 14
Wiput Pootong (60070090)
Median
"""

def main():
    """ Calculate median """
    count = int(input())
    numbers = []

    for _ in range(count):
        numbers.append(int(input()))

    numbers.sort()

    if count % 2 == 0:
        result = numbers[count // 2] + numbers[(count // 2) - 1]

        result /= 2
    else:
        result = numbers[(count // 2)]

    print("%.01f" %result)

main()
