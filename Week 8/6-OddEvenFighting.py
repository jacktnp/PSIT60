""" PSIT Week 8
Wiput Pootong (60070090)
OddEvenFighting
"""
def main():
    """ Count odd and even score then decide winner """

    # Initialize list to collect fighters
    fighters = []
    # Initialize score variable to store team score
    odd_score = 0
    even_score = 0

    # Loop until user input 0 into program
    while True:
        member = int(input())
        # If input 0 into program break loop
        if member == 0:
            break
        # If not 0 insert new fighter into list
        fighters.append(member)

    # Loop into fighters
    for fighter in fighters:
        # If fighter is even give score to even team
        if fighter % 2 == 0:
            even_score += fighter
        # If fighter is odd give score to odd team
        else:
            odd_score += fighter

    # Odd team score is higher than even team : Odd win
    if odd_score > even_score:
        print("Odd %d" %odd_score)
    # Even team score is higher than odd team : Even win
    elif even_score > odd_score:
        print("Even %d" %even_score)
    # Both two teams has the same score : Draw
    else:
        print("Draw %d" %even_score)

main()
