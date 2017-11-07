""" PSIT Week 12
Wiput Pootong (60070090)
RemoveTag
"""

def flatten(text):
    """ Make nested list flatten """
    # Use isinstance() to verify list inside text
    if isinstance(text, list):
        # If it is blank list
        if len(text) == 0:
            return []
        # Flat first member of list and rest of list
        first, rest = text[0], text[1:]
        return flatten(first) + flatten(rest)
    else:
        # When all of members in numbers is flatten return list of numbe
        return [text]

def main():
    """ Clean up text """

    text = input()

    remember = False
    temp = ""

    result = []

    for char in text:
        # Close tag mean begin to remember
        if char == ">":
            remember = True
            continue
        # Open tag mean end to remember
        if char == "<":
            # Check if something in temp append to list
            if temp != "":
                result.append(temp)
                temp = ""
            remember = False
            continue
        # If remember set to True save char in temp
        if remember:
            temp += char

    # If all of text is a plain text mean no tags
    if result == [] and "<" not in text and ">" not in text:
        result = text.split()

    # Strip the text and split into list
    result = [x.strip().split() for x in result]

    # Use custom flatten function to cleanup nested list
    result = flatten(result)

    # Print result
    print(result)

main()
