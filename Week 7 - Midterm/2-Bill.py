""" PSIT Week 7 (Midterm)
Wiput Pootong (60070090)
Bill
"""

def main():
    """ Calculate summary price with service and tax """

    price = int(input())

    # Calculate service charge using min max because service will charge minimum of 50
    # and maximum of 1000
    serivce = min(max(price * 0.1, 50), 1000)

    # Add service into price before calculate tax
    price += serivce

    # Include 7% VAT
    price *= 1.07

    # Print summary only 2 decimals
    print("%.2f" %price)

main()
