"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
    * 1 <= strs.length <= 104
    * 0 <= strs[i].length <= 100
    * strs[i] consists of lowercase English letters.
"""

from typing import List
from collections import defaultdict


# Time Complexity: O(m * n)
#   * m = number of input strings given
#   * n = characters in each string
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # Initialize a result map
    # Mapping the character count to the list of anangrams
    res = defaultdict(list)

    for s in strs:
        # Initalize a list of zeroes for each potential letter in alphabet
        count = [0] * 26 # a ... z

        # Count the number of times a character appearrs in a string
        for c in s:
            # Increment count position for each character in the string
            # The ord() function returns an integer representing the Unicode character.
            # Examples:
            #   * ord("a") - ord("a") = 0
            #   * ord("z") - ord("a") = 25
            count[ord(c) - ord("a")] += 1

        # In Python a list cannot be a key so must convert to tuple
        res[tuple(count)].append(s)

    # Return the values from the dictionary
    return res.values()
