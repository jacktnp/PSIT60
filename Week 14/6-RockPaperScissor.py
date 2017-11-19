""" PSIT Week 14
Wiput Pootong (60070090)
RockPaperScissor
"""

def main():
    """ Count score """
    activity = input()

    score_a = 0
    score_b = 0

    for i in range(0, len(activity), 2):
        # Draw
        if activity[i:i+2] in ["SS", "RR", "PP"]:
            continue
        # A Win
        if activity[i:i+2] in ["RS", "SP", "PR"]:
            score_a += 1
        # B Win
        if activity[i:i+2] in ["SR", "PS", "RP"]:
            score_b += 1

    # A Win
    if score_a > score_b:
        print("A win %d-%d" %(score_a, score_b))
    # B Win
    elif score_b > score_a:
        print("B win %d-%d" %(score_b, score_a))
    # Draw
    else:
        print("DRAW %d" %score_a)


main()
