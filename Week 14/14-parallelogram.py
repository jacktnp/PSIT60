""" PSIT Week 14
Wiput Pootong (60070090)
Parallelogram
"""

def main():
    """ Display parallel """
    text = input()

    for i in range(1, len(text) + 1):
        print(" " * (len(text) - i), text[:i], sep='')
    for i in range(1, len(text)):
        print(text[i:])

main()
