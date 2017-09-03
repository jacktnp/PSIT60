""" Week 3
Wiput Pootong (60070090)
"""

def main():
    """ Print 3 number by condition (ascend or decend) """
    choice = input()

    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    high = find_highest(num1, num2)
    high = find_highest(high, num3)

    low = find_lowest(num1, num2)
    low = find_lowest(low, num3)

    if num1 != high and num1 != low:
        remain = num1
    elif num2 != high and num2 != low:
        remain = num2
    else:
        remain = num3


    if choice == "Ascend":
        print("%.2f, %.2f, %.2f" %(low, remain, high))
    else:
        print("%.2f, %.2f, %.2f" %(high, remain, low))

def find_highest(num1, num2):
    """ Find the highest of 2 numbers """
    if num1 > num2:
        return num1
    return num2

def find_lowest(num1, num2):
    """ Find the lowest of 2 numbers """
    if num1 < num2:
        return num1
    return num2

main()
