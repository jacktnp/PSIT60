""" PSIT Week 10
Wiput Pootong (60070090)
Classify
"""

def main():
    """ Classify Student by id """

    classify = {}

    while 1:
        std_id = input()

        if std_id == "END":
            break

        year = int(std_id[:2])
        faculty = int(std_id[2:4])

        if year not in classify:
            classify[year] = {}
        if faculty not in classify[year]:
            classify[year][faculty] = 0
        classify[year][faculty] += 1

    for year in sorted(classify):
        header = True
        for faculty in sorted(classify[year]):
            if header:
                print("%d %d %d" %(year, faculty, classify[year][faculty]))
                header = False
            else:
                print("-- %d %d" %(faculty, classify[year][faculty]))


main()
