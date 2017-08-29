""" Pair Programming
Wiput Pootong (60070090)
Siwakorn Lertamnuaylap (60070095)
"""

import math

def main():
    """ Math calculation function """
    function1 = (math.sin(90 * math.pi / 180) + math.sin(60 * math.pi / 180)**2) \
    / (math.cos(245**2 * math.pi / 180) + math.cos((45 + 135) * math.pi / 180))
    function2 = (math.factorial(16) * math.factorial(4)) / math.factorial(8)
    function3 = (15 + 25) / math.sqrt((25 - 12) ** 2 + (12 - 15) ** 2)
    function4 = math.log(1234 ** 4, 10)
    function5 = (math.log(4234, 5) + math.log(8191, 2) + 71*math.log(156154, 10)) \
    / (math.log(777, 7) - math.log(888, 8) - math.log(999, 9))

    print(function1)
    print(function2)
    print(function3)
    print(function4)
    print(function5)

main()
