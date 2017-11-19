""" PSIT Week 14
Wiput Pootong (60070090)
Lab_BrickBridge
"""

def main():
    """ Calculate that can do bridge or not """
    small = int(input())
    large = int(input())
    goal = int(input())

    if goal >= (large * 5):
        result = large
    else:
        result = goal // 5
    reminder = goal - (result * 5)

    if reminder > small:
        print(-1)
    else:
        print(reminder)

main()
