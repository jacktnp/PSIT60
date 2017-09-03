""" Week 3
Wiput Pootong (60070090)
"""

def main():
    """ Calculate grade by condition """
    score = float(input())

    if 0 <= score < 60:
        print("F")
    elif 60 <= score < 65:
        print("F+")
    elif 65 <= score < 70:
        print("D")
    elif 70 <= score < 75:
        print("D+")
    elif 75 <= score < 80:
        print("C")
    elif 80 <= score < 85:
        print("C+")
    elif 85 <= score < 90:
        print("B")
    elif 90 <= score < 95:
        print("B+")
    elif 95 <= score <= 100:
        print("A")
    else:
        print("ERR")

main()
