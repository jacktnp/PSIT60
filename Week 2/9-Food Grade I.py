""" Pair Programming
Wiput Pootong (60070090)
Siwakorn Lertamnuaylap (60070095)
"""

def main():
    """count good chicken wings"""
    result = 0
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    result += weight(int(input()))
    print(result)

def weight(num):
    """calculate weight"""
    if 50 <= num <= 70:
        return 1
    return 0

main()
