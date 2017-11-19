""" PSIT Week 14
Wiput Pootong (60070090)
FOR!F-Ball
"""

def main():
    """ Find ball location """

    balls = [1, 0, 0]

    operations = input()

    for char in operations:
        if char == "A":
            balls[0], balls[1] = balls[1], balls[0]
        if char == "B":
            balls[1], balls[2] = balls[2], balls[1]
        if char == "C":
            balls[0], balls[2] = balls[2], balls[0]

    print(balls.index(1) + 1)

main()
