""" Week 6 PSIT 2017
Pressurize """

def main():
    """ Calculate absolute pressure """
    inside = float(input())
    outside = float(input())

    diff = (outside - inside) / inside * 100

    if outside - inside < 0 and abs(diff) > 30:
        print("Underpressure %.04f%%" %(abs(diff)))
    elif outside - inside > 0 and abs(diff) > 30:
        print("Overpressure %.04f%%" %(abs(diff)))
    else:
        print("Safe %.04f%%" %(abs(diff)))

main()
