""" PSIT Week 8
Wiput Pootong (60070090)
AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain
"""

def main():
    """ Display only word with 2 or more vowels """

    # Get string input and remove . then split into list
    text = input().replace('.', '').split()

    # Initialize result list
    result = []

    # Loop text list
    for word in text:
        # Initialize vowels count to 0
        vowels = 0
        # Loop character in word
        for char in word:
            # If character is vowels count vowels
            if char in "aeiou":
                vowels += 1
        # If vowels count is more or equal to 2 add word to result list
        if vowels >= 2:
            result.append(word)
    # Print sorted result list
    for word in sorted(result):
        print(word)

    # If nothing in result list print Nope
    if len(result) == 0:
        print("Nope")

main()
