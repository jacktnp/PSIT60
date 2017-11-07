""" PSIT Week 10
Wiput Pootong (60070090)
AlmostMean
"""

def main():
    """ Find student who nearest to mean """

    scores = {}

    # Get input
    amount = int(input())

    for _ in range(amount):
        key, value = input().split('\t')
        scores[key] = float(value)

    mean = sum(scores.values()) / len(scores)

    first = True
    for key in scores:
        if first and scores[key] <= mean:
            diff = mean - scores[key]
            diff_key = key
            first = False
        if scores[key] <= mean and mean - scores[key] <= diff:
            diff = mean - scores[key]
            diff_key = key

    print("%s\t%.4f" %(diff_key, scores[diff_key]))

main()
