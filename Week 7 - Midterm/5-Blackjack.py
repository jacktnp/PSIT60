""" PSIT Week 7 (Midterm)
Wiput Pootong (60070090)
Blackjack
"""

def main():
    """ Calculate the best backjack points """

    # Get how many card will get
    amount = int(input())

    # Initialize score variable to collect score
    score = 0

    # Initialize ace to collect how many ace will get
    ace = 0

    # Get card for amount times
    for _ in range(amount):
        # Get card
        card = input()

        # score +10 when get J Q K card
        if card in "JQK":
            score += 10

        # score +11 and count ace +1 when get A card
        elif card == "A":
            ace += 1
            score += 11

        # add score depend on number on card
        else:
            score += int(card)

    # Score -10 and Ace count -1 until ace is zero or score under 21
    while score > 21 and ace > 0:
        score -= 10
        ace -= 1

    # Print the best score
    print(score)

main()
