""""
Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
    * 1 <= s.length, t.length <= 5 * 104
    * s and t consist of lowercase English letters.

Follow up:
    * What if the inputs contain Unicode characters?
    * How would you adapt your solution to such a case?
"""


# Algorithm(s) Used: Sorting
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
def isAnagramI(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# Algorithm(s) Used: Counter
# Time Complexity: O(n)
# Space Complexity: O(1)
def isAnagramII(s: str, t: str) -> bool:
    from collections import Counter

    return Counter(s) == Counter(t)


# Algorithm(s) Used: Two Passes, Hash Map
# Time Complexity: O(n) = O(s)
# Space Complexity: O(n) = O(s + t)
def isAnagramIII(s: str, t: str) -> bool:
    if len(s)!= len(t):
        return False

    seenS, seenT = {}, {}

    for i in range(len(s)):
        seenS[s[i]] = seenS.get(s[i], 0) + 1
        seenT[t[i]] = seenT.get(t[i], 0) + 1

    for c in seenS:
        if seenS[c] != seenT.get(c, 0):
            return False

    return True


# Algorithm(s) Used: Two Passes, Hash Map
# Time Complexity: O(n) = O(s)
# Space Complexity: O(n)
def isAnagramIV(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    mapper = {}

    for i in range(len(s)):
        mapper[s[i]] = mapper.get(s[i], 0) + 1

    for i in range(len(t)):
        mapper[t[i]] = mapper.get(t[i], 0) - 1

    return all([x == 0 for x in mapper.values()])


if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "a", True),
        ("ab", "ba", True),
        ("abc", "ab", False),
        ("aa", "bb", False),
        ("listen", "silent", True),
    ]

    funcs = [
        isAnagramI,
        isAnagramII,
        isAnagramIII,
        isAnagramIV
    ]

    for func in funcs:
        for s, t, expected in test_cases:
            assert func(s, t) == expected
