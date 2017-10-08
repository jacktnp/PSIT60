""" PSIT Week 7 (Midterm)
Wiput Pootong (60070090)
Frame
"""

def main():
    """ Print expandable frame with input text inside """

    text = input()

    # Top line
    print("*" * (len(text) + 2))
    # Middle line with text
    print("*", text, "*", sep='')
    # Bottom line
    print("*" * (len(text) + 2))

main()
