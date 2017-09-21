""" Week 6 PSIT 2017
Align """

def main():
    """ Print text align """
    space = int(input())
    align = input()
    text = input()

    if align == "center":
        print(" " * ((space - len(text)) // 2 + (space - len(text)) % 2) + text \
        + " " * ((space - len(text)) // 2))
    elif align == "right":
        print(" " * (space - len(text)) + text)
    elif align == "left":
        print(text)

main()
