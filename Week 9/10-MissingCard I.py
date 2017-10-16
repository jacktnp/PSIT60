""" PSIT Week 9
Wiput Pootong (60070090)
MissingCard I
"""

def main():
    """ Find which card is missing """

    # Cards collection to find which is missing
    cards = []

    # Initialize all cards
    categories = ['S', 'H', 'D', 'C']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    # Get 51 cards
    for _ in range(51):
        cards.append(input())

    # Concat value and category and check in collections on hand or not
    for category in categories:
        for value in values:
            # If not in collection print and completed!
            if (value + category) not in cards:
                print(value + category)
                break

main()
