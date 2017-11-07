""" PSIT Week 12
Wiput Pootong (60070090)
BreakPassword
"""

import hashlib

def main():
    """ Decode SHA-512 password """

    encrypt = input()

    for count in range(100000):
        number = ("0" * (5 - len(str(count))) + str(count))
        password = hashlib.sha512(bytes(number, "utf-8")).hexdigest().upper()
        if password == encrypt:
            print(number)
            break

main()
