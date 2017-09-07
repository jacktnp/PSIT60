"""
    Quest : SceneSwitch I
    Date :  7 SEP 2017
    Pair : Wiput & Apisit
"""
def main():
    """ Switch """
    # 0 = off, 1 = on
    turn = 0
    # 0 = cool, 1 = warm
    warm = 0
    # warm count
    count = 0
    while True:
        time = input()

        if time == "End":
            break

        time = float(time)

        if time == 0:
            turn = 1
            continue

        # Turn off light
        if turn == 1:
            turn = 0
            last = time
            continue

        # Turn on light when turn off more than 6 secs last time not warm
        if turn == 0 and time - last > 6:
            warm = 0
            turn = 1

        # Trun on light when turn off less than 6 sec last time not warm
        if turn == 0 and time - last <= 6 and warm == 0:
            warm = 1
            turn = 1
            count += 1

        # Trun on light when turn off less than 6 sec last time warm
        if turn == 0 and time - last <= 6 and warm == 1:
            warm = 0
            turn = 1


    print(count)
main()
