"""
Cracking the Coding Interview: 1.3

URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string.

Example:
Input:  "Mr John Smith    ", 13
Output: "My%20John%20Smith"
"""


# Algorithms Used: HashMap
# Time Complexity: O(n)
# Memory Complexity: O(1)
def URLify(input_str: str, input_length: int) -> str:
    # Convert input string to a list of chars since STRINGS ARE IMMUTABLE
    input_str = list(input_str)

    # Count the number of spaces (maybe move to function)
    numSpaces = 0
    for i in range(input_length):
        if input_str[i] == " ":
            numSpaces += 1

    # Two extra characters are needed for each space since the substring
    # '%20' is two characters longer than the initial whitespace char
    newIndex = input_length - 1 + numSpaces * 2

    # If there are excess spaces, add a null character.
    # This indicates that the spaces after that point have not been replaced with %20.
    if (newIndex + 1) < len(input_str):
        input_str[newIndex + 1] = '\0'

    # Walk backwards through the string, editing it.
    # If there is a space, replace it with '%20'.
    # If there is no space, then copy the original character.
    for oldIndex in range(input_length - 1, 0, -1):
        if input_str[oldIndex] == ' ':
            # input_str[newIndex] = '0'
            # input_str[newIndex - 1] = '2'
            # input_str[newIndex - 2] = '%'
            input_str[newIndex - 2:newIndex + 1] = '%20'

            newIndex -= 3
        else:
            input_str[newIndex] = input_str[oldIndex]

            newIndex -= 1

    # Convert list of chars back into string
    input_str = ''.join(input_str)
