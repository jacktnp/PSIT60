""" Pair Programming
Wiput Pootong (60070090)
Siwakorn Lertamnuaylap (60070095)
"""

def main():
    """calculate days hours minutes and seconds"""
    time = int(input())
    temp = time
    days = time // 86400
    time %= 86400
    hours = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    if days > 9999 or temp < 0:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d" %(days, hours, minutes, seconds))

main()
