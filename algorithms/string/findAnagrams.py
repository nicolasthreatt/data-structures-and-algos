"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

 
Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
    * 1 <= s.length, p.length <= 3 * 104
    * s and p consist of lowercase English letters.
"""

from typing import List


# Algorithm Used: Sliding Window
# Time Complexity: O(s)
# Space Complexity: O(1)
def findAnagrams(s: str, p: str) -> List[int]:
    # If the anagram substring is longer the the input string
    # return an empty list. This is because the input string but 
    # at-least the size of the anagram string
    if len(p) > len(s): return []

    # Initialize two empty dictionaries.
    # Both to store the counts of each string (p and s)
    sCount, pCount = {}, {}

    # Grab the first set of potential anagram characters from the two input strings
    for i in range(len(p)):
        pCount[p[i]] = pCount.get(p[i], 0) + 1
        sCount[s[i]] = sCount.get(s[i], 0) + 1

    # If the two maps are equal at the starting index, then create a list with the
    # starting index
    res = [0] if sCount == pCount else []

    # Sliding Window Algorithm:
    #    Set left to 0 and loop through the input string with right
    #    For each iteration count the number of characters and increment left
    #    If the two maps are equal, then add the left index to the result list
    l = 0
    for r in range(len(p), len(s)):
        sCount[s[r]] = sCount.get(s[r], 0) + 1
        sCount[s[l]] -= 1


        if sCount[s[l]] == 0:
            sCount.pop(s[l])
        
        l += 1

        if sCount == pCount:
            res.append(l)

    return res