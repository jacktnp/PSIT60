""" PSIT Week 13
Wiput Pootong (60070090)
PairNumbering
"""

import json

def main():
    """ Calculate pair numbering """

    list_a = json.loads(input())
    list_b = json.loads(input())
    expect = int(input())

    list_a = sorted([x for x in list_a if x <= expect])

    count = 0
    for num_a in list_a:
        if expect - num_a in list_b:
            count += list_b.count(expect - num_a)

    print(count)

main()
