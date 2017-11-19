""" PSIT Week 14
Wiput Pootong (60070090)
Roman
"""

def value(roman):
    """ Get value of roman """
    if roman == 'I':
        result = 1
    elif roman == 'V':
        result = 5
    elif roman == 'X':
        result = 10
    elif roman == 'L':
        result = 50
    elif roman == 'C':
        result = 100
    elif roman == 'D':
        result = 500
    elif roman == 'M':
        result = 1000
    else:
        result = -1

    return result

def main():
    """ Convert Roman to Decimal """
    roman = input()

    result = 0
    count = 0

    while count < len(roman):
        sym1 = value(roman[count])

        if count + 1 < len(roman):
            sym2 = value(roman[count + 1])

            if sym1 >= sym2:
                result += sym1
                count += 1
            else:
                result += (sym2 - sym1)
                count += 2
        else:
            result += sym1
            count += 1

    print(result)

main()
