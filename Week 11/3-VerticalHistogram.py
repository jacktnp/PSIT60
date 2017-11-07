""" PSIT Week 11
Wiput Pootong (60070090)
VerticalHistogram
"""

def main():
    """ Main function """
    text = input()

    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = {}

    # loop in alphabets to proof that sorted
    for alpha in alphabets:
        result[alpha] = 0
        for char in text:
            if char == alpha:
                result[alpha] += 1

    # Find maximum
    maximum = result[max(result, key=result.get)]
    # Create chart
    for count in range(maximum, 0, -1):
        print("%03d" %count, end='')
        for alpha in alphabets:
            if result[alpha] >= count and result[alpha] != 0:
                print(" *", end='')
            elif result[alpha] == 0:
                continue
            else:
                print("  ", end='')
        print()
    # Display lastline
    print(" " * 3, end='')
    for alpha in alphabets:
        if result[alpha] != 0:
            print(" %s" %alpha, end='')

main()
