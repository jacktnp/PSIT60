""" Week 4
Wiput Pootong (60070090)
"""

def main():
    """ Find average grade """
    subject = int(input())
    grade = 0

    for _ in range(subject):
        score = float(input())
        if 95 <= score <= 100:
            grade += 4
        elif 90 <= score < 95:
            grade += 3.5
        elif 85 <= score < 90:
            grade += 3
        elif 80 <= score < 85:
            grade += 2.5
        elif 75 <= score < 80:
            grade += 2
        elif 70 <= score < 75:
            grade += 1.5
        elif 65 <= score < 70:
            grade += 1
        elif 60 <= score < 65:
            grade += 0.5

    average = grade / subject
    average = average * 100 // 1 / 100

    print("%.2f" %average)

main()
