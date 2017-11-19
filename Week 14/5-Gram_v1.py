""" PSIT Week 14
Wiput Pootong (60070090)
Gram_v1
"""

def main():
    """ Count the most two gram """
    sentence = input()
    result = [None, 0]

    for i in range(0, len(sentence) - 1):
        count = scheck(sentence, sentence[i:i+2])
        if count > result[1]:
            result[0], result[1] = sentence[i:i+2], count

    print(result[0])
    print(result[1])


def scheck(string, check):
    """ Check and count """
    count = 0
    for i in range(0, len(string) - 1):
        if string[i:i+2] == check:
            count += 1
    return count

main()
