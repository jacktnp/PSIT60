""" PSIT Week 10
Wiput Pootong (60070090)
Filter
"""

import json

def main():
    """ Filter print content """

    # Get input
    score = json.loads(input())
    minimum = float(input())

    result = {}

    # Filter dict and add to result
    for key in score:
        if score[key] > minimum:
            result[key] = score[key]

    # If no result
    if len(result) == 0:
        print("Nope")
    else:
        # Has result print key and result in sort by id
        for key in sorted(result):
            print("%s\t%.2f" %(key, result[key]))

main()
