"""
https://leetcode.com/problems/repeated-dna-sequences/

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long
sequences (substrings) that occur more than once in a DNA molecule.

You may return the answer in any order.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:
    * 1 <= s.length <= 105
    * s[i] is either 'A', 'C', 'G', or 'T'.
"""

from typing import List


# Algorithm Used: Sliding Window
# Time Complexity: O(s)
# Space Complexity: O(s) 
def findRepeatedDnaSequences(s: str) -> List[str]:
    sequence_length = 10
    seen, repeated = set(), set()

    l = 0
    for r in range(len(s)):
        if (r - l + 1 == sequence_length):
            current = s[l:r + 1]
            
            if current in seen:
                repeated.add(current)
            
            seen.add(current)
            l += 1
    
    return repeated
