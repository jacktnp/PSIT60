""" Week 6 PSIT 2017
RuleofThree """

def main():
    """ Calculate the best value price """
    amount = int(input())

    for count in range(amount):
        price = float(input())
        weight = float(input())

        if count == 0:
            best_price = price
            best_weight = weight

        if (price / weight) <= (best_price / best_weight):
            best_price = price
            best_weight = weight

    print("%.2f %.2f" %(best_price, best_weight))

main()
