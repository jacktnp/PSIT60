""" PSIT Week 11
Wiput Pootong (60070090)
LineSorting
"""

def main():
    """ Main function """
    count = int(input())

    strings = []

    for _ in range(count):
        strings.append(input())

    for word in sorted(strings, key=len):
        print(word)

main()
