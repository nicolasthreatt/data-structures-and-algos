"""
https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Example 1:
Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".

Example 2:
Input: s = "010"
Output: 0
Explanation: The string is already alternating.

Example 3:
Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".

Constraints:
    * 1 <= s.length <= 105
    * s[i] is either '0' or '1'.
"""


# Algorithm Used: Sliding Window
# Time Complexity: O(s)
# Space Complexity: O(1)
def minFlips(s: str) -> int:
    # Target Window Length
    n = len(s)

    # Concatenate s with itself (Type-I)
    s = s + s

    # Create the two alternating strings
    alt1, alt2 = "", ""
    diff1, diff2 = 0, 0
    for i in range(len(s)):
        alt1 += "0" if i % 2 else "1"
        alt2 += "1" if i % 2 else "0"
    
    # Set the result variable initially to be some extremely high number,
    # since the objective if to find the MINIMUM number of flips
    res = float('inf')

    # Sliding Window Algorithm:
    #    - Initialize left index to the start index of the string 
    #    - Iterate through input string using right index
    #    - Increment the difference variables if the right index of the
    #      input string does not match the right element of the alternating strings
    #    - If the current window size is GREATER than the input string length, 
    #      then decrement the difference variables and increment left index one position
    #    - If the current window size is EQUAL to the input string length, 
    #      then determine the minimum difference
    l = 0
    for r in range(len(s)):
        # Count the number of differences there are between the input string
        # and the the two seperate alternating strings
        if s[r] != alt1[r]:
            diff1 += 1
        if s[r] != alt2[r]:
            diff2 += 1

        # Update differences and left index if window size becomes out of range
        # current_window_length = r - l + 1
        if (r - l + 1) > n:
            if s[l] != alt1[l]:
                diff1 -= 1
            if s[l] != alt2[l]:
                diff2 -= 1
            l += 1

        # Update result once the window size equals size of the input string
        if (r - l + 1) == n:
            res = min(res, diff1, diff2)
    
    return res
