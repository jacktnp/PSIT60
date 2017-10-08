""" PSIT Week 7 (Midterm)
Wiput Pootong (60070090)
Fizz Buzz
"""

def main():
    """ Print Fizz Buzz from 1 to n """

    # Get fizz buzz limit
    limit = int(input())

    # Count from 1 to limit
    for count in range(1, limit + 1):
        # Count can be divide by 3 and 5
        if count % 3 == 0 and count % 5 == 0:
            print("Fizz Buzz")
        # Count can divide by 3
        elif count % 3 == 0:
            print("Fizz")
        # Count can divide by 5
        elif count % 5 == 0:
            print("Buzz")
        # Count can't divide with 3 and 5 print out count
        else:
            print(count)

main()
