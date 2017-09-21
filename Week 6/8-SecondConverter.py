""" Week 6 PSIT 2017
SecondConverter """

def main():
    """ Convert Second to H:M:S """

    amount = int(input())

    seconds = int(input())
    minutes = int(input())
    hours = int(input())

    r_hours = amount // (minutes * seconds)
    amount -= r_hours * minutes * seconds
    r_hours %= hours
    r_minutes = amount // seconds
    amount -= r_minutes * seconds

    print("%d:%d:%d" %(r_hours, r_minutes, amount))

main()
