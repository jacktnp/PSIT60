""" PSIT Week 9
Wiput Pootong (60070090)
LetterFrequency
"""

def main():
    """ Display the most frequency """

    # Get text and convert to lowercase
    text = input().lower()

    # Collect counting
    count = {}

    # Count char count
    for char in text:
        # Filter which is not character
        if char.isalpha() is False:
            continue
        # If key is not exist
        if char not in count:
            count[char] = 0
        count[char] += 1

    # Print result in max function get key by maximum value
    print(max(count, key=count.get))


main()
