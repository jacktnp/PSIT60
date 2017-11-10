""" PSIT Week 13
Wiput Pootong (60070090)
caesarV1
"""

def main():
    """ Find sum of curcular prime """
    caesar = int(input())
    text = input()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()

    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += upper[(upper.index(char) + caesar) % 26]
                continue
            else:
                result += lower[(lower.index(char) + caesar) % 26]
                continue
        result += char

    print(result)

main()
