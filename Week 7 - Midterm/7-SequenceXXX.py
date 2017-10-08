""" PSIT Week 7 (Midterm)
Wiput Pootong (60070090)
Sequence XXX
"""

def main():
    """ Print the shape with size and times """

    # Get Size of shape
    size = int(input())
    # Amount that will print
    amount = int(input())

    # First count rows
    for row in range(size):
        # Count how many that will print per line depend on amount
        for _ in range(amount):
            # Count columns
            for column in range(size):
                # First line or top border
                condition = (row == 0)
                # Last line or bottom border
                condition += (row == (size - 1))
                # First column or left border
                condition += (column == 0)
                # Last column or right border
                condition += (column == (size - 1))
                # Cross shape from left to right
                condition += (row == column)
                # Cross shape from right to left
                condition += (column == (size - 1 - row))

                # When condition become true condition need to be not 0
                if condition:
                    print("*", end="")
                # Condition is 0 mean false
                else:
                    print(end=" ")
            # Seperate the shape on the same row
            print(end=" ")
        # End of a row
        print()

main()
