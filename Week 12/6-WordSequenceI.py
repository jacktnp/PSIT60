""" PSIT Week 12
Wiput Pootong (60070090)
WordSequence I
"""

def main():
    """ Print word sequences """

    # Get word
    word = input()

    # Print word sequence
    for count in range(1, len(word) + 1):
        print(word[:count])

main()
