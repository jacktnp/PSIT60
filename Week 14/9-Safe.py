""" PSIT Week 14
Wiput Pootong (60070090)
Safe
"""

def main():
    """ Calculate how many time to open safe """

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    password = input()
    lock = input()

    result = 0

    for i in range(len(password)):
        if password[i] == lock[i]:
            continue
        diff = abs(alpha.index(password[i]) - alpha.index(lock[i]))
        result += min(diff, 26 - diff)

    print(result)

main()
