"""
Cracking the Coding Interview: 1.5

One Away: There are three types of edits that can be performed on string:
    - Insert a character
    - Remove a character
    - Replace a character
Give two ostrings, write a function to check if there are one dit (or zero edits away)

Example:
pale, ple -> True
pales, pale -> True
pale, bale -> True
pale, bake -> False
"""

# Algorithm Used: Iteration
# Time Complexity: O(n), where n is dependent on str1
# Memory Complexity: O(1)
def oneAway(str1, str2):

    # Initialize a variable to count the number of differences between the two strings
    # If the two strings sizes differ by two, then set the value to infinity since no
    # operation can be completed
    diffs = 0 if len(str1) - 1 <= len(str2) <= len(str1) + 1 else float('inf')

    # Now that we already know if the two strings are differ in length by more than 1,
    # we only need to check the characters relating to one of the strings.
    # Determine the number of differences between the two strings
    for i in range(len(str1)):
        if str1[i] not in str2:
            diffs += 1
    
    # For all three operations (insert, remove, or replace)
    # there can be at-most 1 difference between the two strings
    # If there are no difference and the lengths differ by only one, then strings are the same
    return 0 <= diffs <= 1
