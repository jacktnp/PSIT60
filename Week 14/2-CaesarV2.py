""" PSIT Week 14
Wiput Pootong (60070090)
CaesarV2
"""

def main():
    """ Count the most two gram """
    encoded = input()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()

    words = ['The', 'the', 'What', 'what', 'Where', 'where', 'When', 'when']
    result = ""
    while 1:
        for char in encoded:
            if char.isupper():
                result += upper[(upper.index(char) + 1) % 26]
            elif char.islower():
                result += lower[(lower.index(char) + 1) % 26]
            else:
                result += char
        encoded = result
        if check(result, words):
            break
        result = ""
    print(encoded)


def check(result, words):
    """ Check word is in sentence """
    for word in words:
        if word in result:
            return True
    return False



main()
