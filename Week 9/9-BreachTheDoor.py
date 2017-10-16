""" PSIT Week 9
Wiput Pootong (60070090)
BreachTheDoor
"""

def main():
    """ Display word that more than 6 characters """

    # Get string
    text = input()

    # Select only alphabet
    sentence = ""
    for char in text:
        if char.isalpha() or char == " ":
            sentence += char

    # Split into list
    sentence = sentence.split(' ')

    # Print word that longer than 6 characters
    for word in sentence:
        if len(word) > 6:
            print(word, end=' ')

main()
