""" PSIT Week 12
Wiput Pootong (60070090)
WordSequence II
"""

def main():
    """ Print word sequences """

    # Get word
    word1 = input()
    word2 = input()

    # Calculate max length
    length = max(len(word1), len(word2))

    # Print result using list comp.
    _ = [print(word2[:count] + word1[count:]) for count in range(length + 1)]

main()
