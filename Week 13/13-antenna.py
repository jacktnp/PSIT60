""" PSIT Week 13
Wiput Pootong (60070090)
antenna (AIS Confirmed!)
"""

import json

def main():
    """ Calculate minimum antenna use for 100% coverage """

    # Get inputs
    radius = int(input())

    users = json.loads(input())

    # Sort users positions
    users.sort()

    # If no users!
    if len(users) == 0:
        print(0)
        return

    # Initialize temp to calculate (Using Geedy Algorithms)
    temp = users[0]
    antennas = 1

    for user in users:
        # When out of previous antenna
        if user - temp > radius * 2:
            antennas += 1
            temp = user

    # Print result
    print(antennas)

main()
