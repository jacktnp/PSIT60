""" PSIT Week 9
Wiput Pootong (60070090)
Pick
"""

# Import json library
import json

def main():
    """ Check key in dict is exist or not """

    # Convert string into dict with json.loads()
    data = json.loads(input())

    # Get key that want to find that exist or not?
    key = input()

    # If key is exist
    if key in data:
        print("Yes")
        print(data[key])
    # Not exist
    else:
        print("No")

main()
