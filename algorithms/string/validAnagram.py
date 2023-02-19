""""
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

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


# Time Complexity: O(n) = O(s + t)
# Memory Complexity: O(n) = O(s + t)
def isAnagramI(s: str, t: str) -> bool:
    # Check to see if the two lists are equal length first
    if len(s)!= len(t):
        return False

    # Create a hash map for each input array
    hashS, hashT = {}, {}

    # Index through both arrays and store their values in seperate hash maps
    for i in range(len(s)):
        # Count the number of occurances a key is in the hash map
        hashS[s[i]] = hashS.get(s[i], 0) + 1
        hashT[t[i]] = hashT.get(t[i], 0) + 1

    # Iterate through one of the hash maps and see if the values are equal for each given key
    for c in hashS:
        # Check if the hash map values for a given key is not the same for the two hash maps
        if hashS[c] != hashT.get(c, 0):
            return False

    return True


# Time Complexity: O(n)
# Memory Complexity: O(1)
def isAnagramII(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# Time Complexity: O(n)
# Memory Complexity: O(1)
def isAnagramIII(s: str, t: str) -> bool:
    from collections import Counter

    return Counter(s) == Counter(t)
