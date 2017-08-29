""" Pair Programming
Wiput Pootong (60070090)
Siwakorn Lertamnuaylap (60070095)
"""

def main():
    """ Main function """
    # Average weight
    avg = float(input())

    point1 = float(input())
    point2 = float(input())
    point3 = float(input())
    # Calculate missing point
    point4 = (avg * 4) - (point1 + point2 + point3)


    if avg * 4 >= 15000:
        print("Overweight")
    elif cal_balance(point1, avg) or cal_balance(point2, avg) or \
    cal_balance(point3, avg) or cal_balance(point4, avg):
        print("Unbalance")
    else:
        print("Pass %.2f" %point4)

def cal_balance(weight, average):
    """ Calculate unbalance point """
    if weight <= average - (average / 2) or weight >= average + (average / 2):
        return True
    return False

main()
