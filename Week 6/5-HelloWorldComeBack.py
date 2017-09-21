""" Week 6 PSIT 2017
HelloWorldComeBack """

def main():
    """ Check Thai or English """
    name = input()

    if 65 <= ord(name[0]) <= 122:
        print("Hello %s." %name)
    else:
        print("สวัสดี %s" %name)

main()
