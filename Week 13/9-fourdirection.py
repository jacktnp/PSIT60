""" PSIT Week 13
Wiput Pootong (60070090)
fourdirection
"""

def main():
    """ Print direction """
    direction = input()

    for line in range(1, 6):
        temp = ""
        for char in direction:
            if char == "U":
                temp += up_direction(line)
            if char == "D":
                temp += down_direction(line)
            if char == "L":
                temp += left_direction(line)
            if char == "R":
                temp += right_direction(line)
        print(temp)


def up_direction(line):
    """ Print Up Direction """
    if line == 1 or line == 4 or line == 5:
        return "  *   "
    if line == 2:
        return " ***  "
    if line == 3:
        return "* * * "

def down_direction(line):
    """ Print Down Direction """
    if line == 1 or line == 2 or line == 5:
        return "  *   "
    if line == 3:
        return "* * * "
    if line == 4:
        return " ***  "

def left_direction(line):
    """ Print Left Direction """
    if line == 1 or line == 5:
        return "  *   "
    if line == 2 or line == 4:
        return " *    "
    if line == 3:
        return "***** "

def right_direction(line):
    """ Print Right Direction """
    if line == 1 or line == 5:
        return "  *   "
    if line == 2 or line == 4:
        return "   *  "
    if line == 3:
        return "***** "

main()
