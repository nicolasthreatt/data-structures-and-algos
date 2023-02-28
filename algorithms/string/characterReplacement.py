"""
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after
performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 
Constraints:
    * 1 <= s.length <= 105
    * s consists of only uppercase English letters.
    * 0 <= k <= s.length
"""


# Algorithm Used: Sliding Window
# Time Complexity: O(26*n)
# Space Complexity: O(n)
def characterReplacement(s: str, k: int) -> int:
    # Initialize a map to store the counts of each letter in the input string
    charCountMap = {}

    # Initialize a varaible to keep track of the longest substring
    longest_window = 0

    # Perform Sliding Window Algorithm
    # Start left at the beginning and use right as primary iterator
    l = 0
    for r in range(len(s)):
        # For each input string update the number of occurances for each
        # character in the input string
        charCountMap[s[r]] = charCountMap.get(s[r], 0) + 1

        # Since k is the number of avaiable replacements, check to see if
        # there are any slots for another character to be added to the current
        # substring.
        # This is done by getting the window length (aka the substring length)
        # and substracting the character count from the character with the most occurences.
        # If there are too many open slots in the current window update the left
        # position, along with decremening its count value in the hash map.
        # NOTE: current_window = r - l + 1
        while ((r - l + 1) - max(charCountMap.values())) > k:
            charCountMap[s[l]] -= 1
            l += 1

        # Update the longest window (aka longest substring with k replacements)
        longest_window = max(longest_window, r - l + 1)

    return longest_window
