""" PSIT Week 14
Wiput Pootong (60070090)
War
"""

import json

def main():
    """ Calculate power """

    atkk = json.loads(input())
    deff = json.loads(input())

    ans = 0
    atkk.sort(reverse=True)
    deff.sort(reverse=True)
    for i in deff:
        for j in atkk:
            if j > i:
                ans += j
                atkk.remove(j)
            break
    print(ans)

main()
