"""
Pair Programming : Week 5
60070090 & 60070093
"""

def main():
    """ Print in pattern """
    num = int(input())
    for count in range(num, -num - 1, -1):
        if count == 0 or count == -1:
            continue
        count = abs(count)
        for count2 in range(count, num):
            print("%02d " % count2, end="")
        for count2 in range(num, num - count, -1):
            print("%02d " % count2, end="")
        for count2 in range(num - count + 2, num + 1):
            print("%02d " % count2, end="")
        for count2 in range(num - 1, count - 1, -1):
            print("%02d " % count2, end="")
        print()

main()
