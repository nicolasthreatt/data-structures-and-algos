"""
Cracking the Coding Interview: 1.1

Is Unqiue: Implement an algorithm to determine if a string has all unique characters?
What if you cannot use additional data structures?
"""


# Time Complexity: O(n)
# Space Complexity: O(1) -> charSet will never have over 128 elements
def isUnique(s: str) -> bool:

    # Since there are only 128 "Standard" ASCII characters, if the
    # input string has a greater lenbth of 128 then there is a duplicate.
    # This is the reason why for the space complexity is O(1)
    if len(s) > 128: return False

    # Create a set to keep track of unqiue characters
    charSet = set()

    # Iterate through input string and add characters to the set.
    # If the character is already in the set, then there is a duplicate
    for char in s:
        if char in charSet:
            return False
        charSet.add(char)

    return True
