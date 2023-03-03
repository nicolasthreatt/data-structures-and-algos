"""
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
    * 1 <= s1.length, s2.length <= 104
    * s1 and s2 consist of lowercase English letters.
"""

# Algorithm Used: Hashmap, Sliding Window
# Time Complexity: O(s2)
# Space Complexity: O(1)
def checkInclusion(s1: str, s2: str) -> bool:

    # A permuation cannot be found if the length of s1 is greater than s2
    if len(s1) > len(s2): return False

    # Create two integer arrays, each with a spot for each letter in the alphabet and
    # the number of occurences for each input string for the length of the string
    # that has the permutation requirement (s1)
    s1Count, s2Count = [0] *  26, [0] *  26
    for i in range(len(s1)):
        # The ord() function returns an integer representing the Unicode character.
        # Examples:
        #   * ord("a") - ord("a") = 0
        #   * ord("z") - ord("a") = 25
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    # Count for number of characters that are equal to each other that occured
    # during the length of the string that has the permutation requirement (len(s1))
    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)

    # Sliding Window Algorithm
    # Get the array index from the right pointer
    #   - Using the array index, update the occurence count for s2
    #   - If the number of occurences is equal between the two maps, increment matches
    #   - If the number of occurences is now overflowing, decrement matches
    # Repeat for character at left pointer position
    l = 0
    for r in range(len(s1), len(s2)):
        # Check if the two input strings contain a match for each value in the alphabet
        if matches == 26: return True

        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        l += 1

    # NOTE: After iteration check to length of matches is equal to number of characters in the alphabet
    return matches == 26
