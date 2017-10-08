""" PSIT Week 7 (Midterm)
Wiput Pootong (60070090)
Turnstile
"""

def main():
    """ Count how many people can be pass the door """

    # Initalize logs variable that contain door activity
    logs = ""

    # Got the action until enter "END"
    while True:
        action = input()

        # Break when got action == "END"
        if action == "END":
            break

        # When got action that's not "END" add it into logs
        logs += action

    # Count CP because if user insert coin into door then push it door will allow to pass
    count = logs.count("CP")

    # Print out result
    print(count)

main()
