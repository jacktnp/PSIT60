""" PSIT Week 13
Wiput Pootong (60070090)
olympics
"""

def main():
    """ Calculate minimum antenna use for 100% coverage """

    # Get inputs
    data = int(input())

    score = []

    for _ in range(data):
        score.append([int(x) if x.isdigit() else x for x in input().split()])

    # Sort by index
    score.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))

    # Initalize counting variable
    count = 1
    cache = score[0]
    cout = 0
    first = True

    for result in score:
        # if it's same as before
        if cache[1:] == result[1:]:

            # Print result
            print(count, result[0], result[1], result[2], result[3], sum(result[1:]))

            # If first line
            if first:
                first = False
                cout += 1
                cache = result
                continue

            # Count similar
            cout += 1

            # Store new cache
            cache = result
        # Not same as previous record
        else:
            # Skip similar
            count += cout

            # Reset similar count
            cout = 1

            # Print result
            print(count, result[0], result[1], result[2], result[3], sum(result[1:]))

            # Store new cache
            cache = result

main()
