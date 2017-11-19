""" PSIT Week 14
Wiput Pootong (60070090)
Key_Midterm2014
"""

def main():
    """ Find key """

    number = input()

    key1 = sum([int(x) for x in number])
    key2 = (int(number) % 1000) * 10

    key = key1 + key2

    if key < 1000:
        key += 1000
    print("%04d" %(key % 10000))

main()
