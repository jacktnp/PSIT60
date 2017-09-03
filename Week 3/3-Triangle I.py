""" Week 3
Wiput Pootong (60070090)
"""

def f_srt(num1, num2, num3):
    """ Custom sort function of 3 numbers """
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2

    return num1, num2, num3

def main():
    """ Find vaild triangle """
    var_a, var_b, var_c = float(input()), float(input()), float(input())

    var_a, var_b, var_c = f_srt(var_a, var_b, var_c)

    if abs(var_c ** 2 - (var_a ** 2 + var_b ** 2)) < 0.01:
        print("Yes")
    else:
        print("No")

main()
