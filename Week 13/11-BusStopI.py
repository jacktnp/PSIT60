""" PSIT Week 13
Wiput Pootong (60070090)
BusStop I
"""

def main():
    """ Calculate maximum passengers who can reach destination """

    capacity = int(input())

    stops = int(input())

    bus = []

    passenger = {}

    result = 0

    for _ in range(1, stops + 1):
        data = [int(x) for x in input().split()]
        passenger[data[0]] = [x for x in data[1:] if x >= data[0]]

    for stop in sorted(passenger):
        result += bus.count(stop)
        bus = [x for x in bus if x != stop]
        available = capacity - len(bus)

        bus += passenger[stop][0:available]

    print(result)

main()
