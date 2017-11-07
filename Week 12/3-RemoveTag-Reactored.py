""" PSIT Week 12
Wiput Pootong (60070090)
RemoveTag (Refactored Version)
"""

def main():
    """ Clean up text """

    text = input()

    # Find start of first tag
    start = text.find("<")

    # Loop until can't find tag start mean all tag has been removed!
    while start != -1:
        # Find the end of tag
        end = text.find(">")
        # Remove tag from text by cutout tag replace by space for split
        # Then add remaining text after closing tag
        text = text[:start] + ' ' + text[end + 1:]
        # Find new start tag positon
        start = text.find("<")

    # When all tag has been removed use split convert into list
    result = text.split()

    # Print result
    print(result)

main()
