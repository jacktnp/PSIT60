""" Week 3
Wiput Pootong (60070090)
"""

def main():
    """ Find that working area of machine is intercept or not """
    pos_x1 = float(input())
    pos_y1 = float(input())
    rad_1 = float(input())
    pos_x2 = float(input())
    pos_y2 = float(input())
    rad_2 = float(input())

    if ((pos_x1 - pos_x2) ** 2 + (pos_y1 - pos_y2) ** 2) ** 0.5 < rad_1 + rad_2:
        print("Yes")
    else:
        print("No")

main()
