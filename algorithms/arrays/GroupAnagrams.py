"""
Group Anagrams
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
    * 1 <= strs.length <= 10^4
    * 0 <= strs[i].length <= 100
    * strs[i] consists of lowercase English letters.
"""

from typing import List
from collections import defaultdict


class GroupAnagrams:

    # Algorithm(s) Used: Hash Maps, Sorting
    # Time Complexity: O(n·k·log k), k is average length of a string
    # Space Complexity: O(n)
    def groupAnagramsI(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for anagram in strs:
            key = tuple(sorted(anagram))
            anagrams[key].append(anagram)  # Tuples are Immutable and Hashable Objects

        return list(anagrams.values())

    # Algorithm(s) Used: Hash Maps, Bucketization
    # Time Complexity: O(n·k·log k), k is average length of a string
    # Space Complexity: O(n)
    def groupAnagramsII(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for anagram in strs:
            chars = [0] * 26  # Bucket (count) for each character
            for char in anagram:
                chars[ord(char) - ord('a')] += 1
            
            key = tuple(chars)
            anagrams[key].append(anagram)  # Tuples are Immutable and Hashable Objects

        return list(anagrams.values())


if __name__ == "__main__":
    Solution = GroupAnagrams()

    # (strs, expected)
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat","tea","ate"], ["tan","nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["abc","bca","cab","xyz","zyx"], [["abc","bca","cab"], ["xyz","zyx"]]),
        (["listen","silent","enlist","google","gogole"], [["listen","silent","enlist"], ["google","gogole"]])
    ]

    funcs = [
        Solution.groupAnagramsI,
        Solution.groupAnagramsII,
    ]

    for func in funcs:
        for strs, expected in test_cases:
            result_sorted = sorted([sorted(group) for group in func(strs[:])])
            expected_sorted = sorted([sorted(group) for group in expected])
            assert result_sorted == expected_sorted
