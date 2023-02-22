"""
https://leetcode.com/problems/valid-parentheses/

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


# Data Structured Used: Stack (LIFO)
# Time Complexity: O(n)
# Memory Complexity: O(n)
def isValid(s: str) -> bool:
    # Create a hash map for the specified bracket pairs
    closeToOpenMap = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
    }

    # Initialize a list as a stack
    stack = []

    # Iterate through input string
    for c in s:
        # Check to see if the current character is an opening or closing brack
        # If its a closing bracket, check to see if the stack exist and that the 
        # last element added to the stack is its opening bracket.
        # Note, stacks are LIFO (Last In, First Out)
        if c in closeToOpenMap:
            if stack and stack[-1] == closeToOpenMap[c]:
                stack.pop() # Remove opening bracket from stack once maatch is found
            else:
                return False
        # If its an opening bracket add it to the stack
        else:
            stack.append(c)

    # Remember that the stack is popping off the opening bracket
    # if it finds its closing bracket in the next index. Thus,
    # after iteration stack must be empty.
    return not stack
