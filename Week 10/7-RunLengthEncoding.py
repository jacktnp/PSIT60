""" PSIT Week 10
Wiput Pootong (60070090)
Run Length Encoding
"""

def main():
    """ Encode the text """

    # Get input
    text = input()

    key = []
    value = []

    while text != "":
        count = 0
        for char in text:
            if char != text[0]:
                break
            count += 1
        key.append(text[0])
        value.append(count)
        text = text.lstrip(text[0])

    for count in range(len(key)):
        print("%d%s" %(value[count], key[count]), end='')

main()
