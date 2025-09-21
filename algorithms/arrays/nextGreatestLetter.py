"""
Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target

You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target.
If such a character does not exist, return the first character in letters.

Example 1:
    Input: letters = ["c","f","j"], target = "a"
    Output: "c"
    Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:
    Input: letters = ["c","f","j"], target = "c"
    Output: "f"
    Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:
    Input: letters = ["x","x","y","y"], target = "z"
    Output: "x"
    Explanation: There are no characters in letters that is lexicographically greater than 'z'.

Constraints:
    * 2 <= letters.length <= 10^4
    * letters[i] is a lowercase English letter.
    * letters is sorted in non-decreasing order.
    * letters contains at least two different characters.
    * target is a lowercase English letter.
"""

from typing import List


# Algorithm Used: Binary Search
# Time Complexity: O(log(n))
# Space Complexity: O(1)
def nextGreatestLetter(letters: List[str], target: str) -> str:
    l, r = 0, len(letters) - 1

    # Base Case (Out of Bounds):
    #   - If target is smaller than the first letter
    #   - Or target is greater than or equal to the last letter
    if target < letters[l] or target >= letters[r]:
        return letters[l]
    
    # Binary search for the first letter strictly greater than target
    while l <= r:
        m = (l + r) // 2
        if ord(letters[m]) <= ord(target):
            l = m + 1
        else:
            r = m - 1

    return letters[l]  # 'l' is now first letter greater than target


if __name__ == "__main__":
    # Examples
    assert nextGreatestLetter(["c", "f", "j"], "a") == "c"
    assert nextGreatestLetter(["c", "f", "j"], "c") == "f"
    assert nextGreatestLetter(["c", "f", "j"], "d") == "f"
    assert nextGreatestLetter(["c", "f", "j"], "g") == "j"
    assert nextGreatestLetter(["c", "f", "j"], "j") == "c"  # wrap-around

    # Additional edge cases
    assert nextGreatestLetter(["a", "b"], "z") == "a"       # wrap-around at end
    assert nextGreatestLetter(["a", "b"], "a") == "b"       # exact match then next
    assert nextGreatestLetter(["a", "b"], "b") == "a"       # last element then wrap
    assert nextGreatestLetter(["x"], "x") == "x"            # single element wrap
    assert nextGreatestLetter(["e"], "a") == "e"            # single element, smaller target
    assert nextGreatestLetter(["c", "f", "j"], "k") == "c"  # beyond range then wrap
