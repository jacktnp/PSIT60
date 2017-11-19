""" PSIT Week 14
Wiput Pootong (60070090)
Discount
"""

def main():
    """ Calculate discounted price """

    books = []

    while 1:
        price = input()

        if price == "ENTER":
            break

        books.append(int(price))

    books.sort()

    if len(books) < 20:
        bonus = min(2, len(books) // 6)
    else:
        bonus = len(books) // 5

    print(sum(books[bonus:]))

main()
