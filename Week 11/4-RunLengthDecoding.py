""" PSIT Week 11
Wiput Pootong (60070090)
Run Length Decoding
"""

def main():
    """ Convert encoded string into decoded """
    strings = input()

    counts = []
    chars = []

    temp = ""
    for char in strings:
        if char.isdigit():
            temp += char
        else:
            counts.append(int(temp))
            temp = ""
            chars.append(char)

    result = ""
    for count in range(len(chars)):
        result += (counts[count] * chars[count])

    print(result)

main()
