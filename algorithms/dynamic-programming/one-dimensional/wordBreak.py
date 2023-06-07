"""
https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
    Note that you are allowed to reuse a dictionary word.

Example 3:
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false

Constraints:
    * 1 <= s.length <= 300
    * 1 <= wordDict.length <= 1000
    * 1 <= wordDict[i].length <= 20
    * s and wordDict[i] consist of only lowercase English letters.
    * All the strings of wordDict are unique.
"""


from typing import List


# Algorithm Used: Dynamic Programming, One-Dimensional, Buttom-Up
# Time Complexity: O(n * m)
# Memory Complexity: O(n)
def wordBreak(s: str, wordDict: List[str]) -> bool:
    # Initialize dp array to store whether a substring can be broken down into words.
    #     - dp array will be the size of the string plus one to account for the empty string.
    # dp[i] will be True if the substring starting at index i can be broken down into words.
    dp = [False] * (len(s) + 1)

    # BASE CASE:
    # Empty strings can always be broken down into words, so dp[len(s)] is set to True.
    dp[len(s)] = True

    # Iterate through the string in reverse order.
    # For each character, check if the substring starting at the current character can be broken down into words.
    for current_index in range(len(s) - 1, -1, -1):
        for word in wordDict:
            # Check if the substring starting at the current index plus the length of the word
            # is a valid word in the dictionary and the substring after the word can be broken down into words.
            if (current_index + len(word)) <= len(s) and s[current_index : current_index + len(word)] == word:
                dp[current_index] = dp[current_index + len(word)]

            # If the substring starting at the current index can be broken down into words,
            # then break out of the loop, only need to find one valid word.
            if dp[current_index]:
                break

    # Return whether the substring starting at the first character can be broken down into words.
    return dp[0]
