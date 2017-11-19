""" PSIT Week 14
Wiput Pootong (60070090)
Catalan
"""

def main():
    """ Calculate Catalan """

    catalan = [1]

    count = int(input())

    for i in range(count + 1):
        result = ((4 * i + 2) / (i + 2)) * catalan[i]

        catalan.append(int(result))

    # Print result
    print(catalan[count])

main()
