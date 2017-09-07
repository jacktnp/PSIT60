""" Week 4
Wiput Pootong (60070090)
"""

def main():
    """ Print number from m to n """
    start = int(input())
    stop = int(input())

    if start < stop:
        step = 1
    else:
        step = -1

    for count in range(start, stop + step, step):
        print(count)
main()
