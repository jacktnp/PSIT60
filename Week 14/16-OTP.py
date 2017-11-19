""" PSIT Week 14
Wiput Pootong (60070090)
OTP
"""

def main():
    """ Find valid OTP """
    answer = []
    while 1:
        otp = input()
        if otp == "0":
            break

        if len(otp) == 4:
            answer.append(four_otp(otp))
        elif len(otp) == 6:
            answer.append(six_otp(otp))
        elif len(otp) == 8:
            answer.append(eight_otp(otp))
    for i in answer:
        print(i)


def four_otp(otp):
    """ 4 Digits OTP """
    check = {}
    state = "Invalid"
    for i in otp:
        if i not in check:
            check[i] = 1
        else:
            check[i] += 1
        values_count_2 = list(check.values()).count(2)
    if values_count_2 == 1:
        state = "Valid"

    return state

def six_otp(otp):
    """ 6 Digits OTP """
    check = {}
    state = "Invalid"
    for i in otp:
        if i not in check:
            check[i] = 1
        else:
            check[i] += 1
        values_count_2 = list(check.values()).count(2)
        values_count_3 = list(check.values()).count(3)
    if values_count_2 == 2 and values_count_3 != 1:
        state = "Valid"
    elif values_count_2 != 2 and values_count_3 == 1:
        state = "Valid"

    return state

def eight_otp(otp):
    """ 8 Digit OTP """
    check = {}
    state = "Invalid"
    for i in otp:
        if i not in check:
            check[i] = 1
        else:
            check[i] += 1
        values_count_2 = list(check.values()).count(2)
        values_count_3 = list(check.values()).count(3)
    if values_count_2 == 3 and values_count_3 != 2:
        state = "Valid"
    elif values_count_2 != 3 and values_count_3 == 2:
        state = "Valid"

    return state


main()
