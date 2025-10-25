"""
Valid Parentheses
https://leetcode.com/problems/valid-parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Constraints:
    * 1 <= s.length <= 104
    * s consists of parentheses only '()[]{}'.
"""

from typing import List


# Algorithm Used: Hash-Map, Stack (LIFO)
# Time Complexity: O(n)
# Memory Complexity: O(n)
def isValid(s: str) -> bool:
        brackets = {
            '{': '}',
            '(': ')',
            '[': ']',
        }

        stack = []  # Stack to keep track of opening brackets
        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)  # If it's an opening bracket, push to stack
            else:
                # If there's no opening bracket to match or mismatch found, return False
                if not stack or brackets[stack.pop()] != bracket:
                    return False

        #  If stack is empty, all brackets matched correctly
        return not stack


if __name__ == "__main__":
    # Test cases: (input, expected_output)
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("(((((())))))", True),
        ("(", False),
        (")", False),
        ("", True),
        ("{[()()]}", True),
        ("{[()()]]", False),
    ]

    for s, expected in test_cases:
        result = isValid(s)
        assert result == expected
