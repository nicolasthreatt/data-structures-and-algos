"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
    * 0 <= s.length <= 5 * 104
    * s consists of English letters, digits, symbols and spaces.
"""


# Algorithm Used: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(n)
def lengthOfLongestSubstring(s: str) -> int:
    # Initialize a set to hold the current longest substring
    # while iterating through input string
    charSet = set()

    # Initialize a variable to keep track of the longest substring
    longest_window = 0

    # Start the left pointer at the beginning of the string
    l = 0

    # Iterate through string using the right pointer
    for r in range(len(s)):

        # Look to if the current character from the right window index is in
        # the character set, this means there is a duplicate and thus marking
        # the end of a substring.
        # Countinue to update the left  window index past the duplicate index.
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1

        # Once there are no duplicates in the substring, add the current character
        # to the character set
        charSet.add(s[r])

        # Determine longest window
        current_window = r - l + 1
        longest_window = max(longest_window, current_window)

    return longest_window
