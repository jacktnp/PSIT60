""" PSIT Week 14
Wiput Pootong (60070090)
Kangaroo
"""

def main():
    """ Maximum times kangaroo can jump """
    kangaroo = [int(input()) for _ in range(3)]

    print(max(kangaroo[2] - kangaroo[1], kangaroo[1] - kangaroo[0]) - 1)

main()
