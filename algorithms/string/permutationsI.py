"""
Cracking the Coding Interview: 1.2
    - Given two string, write a method to decide if one is permutation of the other
"""


# Algorithm Used: Hashmap, Sliding Window
# Time Complexity: O(s2)
# Space Complexity: O(1) - Max HashMap size is total number of characters in alphabet
def isPermutation(s1: str, s2: str) -> bool:
     # A permuation cannot be found if the length of s1 is greater than s2
    if len(s1) > len(s2): return False

    # Initialize a variable to keep track of permutation characters
    n = len(s1)

    # Create two maps:
    #   - One to count the occurences of characters in the permutation characters of s1
    #   - One to count the occurences of chars within current window
    charMap1 = {char: 0 for char in range(ord('a'), ord('z') + 1)}
    charMap2 = {char: 0 for char in range(ord('a'), ord('z') + 1)}

    # Update both maps to count the first characters for each string that occur within
    # the length of s1
    for i in range(n):
        charMap1[ord(s1[i])] += 1
        charMap2[ord(s2[i])] += 1

    # Sliding Window Algorithm
    #   - Start the left and right index at the beginning of s2
    #   - Use right index as primary iterator of s2
    #   - Update the number of occurences within each window
    l = 0
    for r in range(n, len(s2)):
        if charMap1 == charMap2:
            return True
        
        charMap2[ord(s2[l])] -= 1
        charMap2[ord(s2[r])] += 1

        l += 1

    # NOTE: After iteration check if the two hash maps are equal
    return charMap1 == charMap2
