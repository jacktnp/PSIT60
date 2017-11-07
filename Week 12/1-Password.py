""" PSIT Week 12
Wiput Pootong (60070090)
Password
"""

import hashlib

def main():
    """ Encode SHA-512 password """

    # Input and print encrypted password
    print(hashlib.sha512(bytes(input(), "utf-8")).hexdigest().upper())

main()
