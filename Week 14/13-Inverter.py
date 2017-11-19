""" PSIT Week 14
Wiput Pootong (60070090)
Inverter
"""

def main():
    """ Calculator Invertor """
    number = input()

    result = ""

    for digit in number:
        if digit == "1":
            result += "0"
        if digit == "0":
            result += "1"

    print(result.lstrip("0"))

main()
