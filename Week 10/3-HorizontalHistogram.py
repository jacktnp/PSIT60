""" PSIT Week 10
Wiput Pootong (60070090)
HorizontalHistogram
"""

def main():
    """ Display histogram of alphabets """

    text = input()

    upper = {}
    lower = {}

    for char in text:
        if char.isupper():
            if char not in upper:
                upper[char] = 0
            upper[char] += 1
        else:
            if char not in lower:
                lower[char] = 0
            lower[char] += 1

    for char in sorted(lower):
        print("%s : " %char, end='')
        for count in range(lower[char]):
            print("-", end='')
            if count % 5 == 4 and count != (lower[char] - 1):
                print("|", end='')
        print()

    for char in sorted(upper):
        print("%s : " %char, end='')
        for count in range(upper[char]):
            print("-", end='')
            if count % 5 == 4 and count != (upper[char] - 1):
                print("|", end='')
        print()


main()
