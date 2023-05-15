"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below:
    * 2 -> abc
    * 3 -> def
    * 4 -> ghi
    * 5 -> jkl
    * 6 -> mno
    * 7 -> pqrs
    * 8 -> tuv
    * 9 -> wxyz

Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
    * 0 <= digits.length <= 4
    * digits[i] is a digit in the range ['2', '9'].
"""

from typing import List


# Algorithm Used: Backtracking, Recursion
# Time Complexity: O(n * 4^n), where
#   - n is the length of the input string
#   - 4^n is the number of combinations
# Space Complexity: O(4^n)
def letterCombinations(digits: str) -> List[str]:
    # Create a dictionary to map digits to letters
    digit_to_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    # Create a list to store all combinations to be returned
    combinations = []

    def dfs(i: int, current_string: str) -> None:
        """Depth-first search helper function. Recursively generate all combinations.

        Args:
            i (int): The current index of the input string.
            current_string (str): The current combination path.
        """

        # BASE CASE:
        #   - If the current combination is the same length as the input string,
        #     append the current combination to the combinations list and return.
        #     This means every digit from the input has been mapped to its respesctive letters
        #     so the current combination is complete.
        if len(current_string) == len(digits):
            combinations.append(current_string)
            return

        # RECURSIVE CASE:
        #   - Iterate through all possible letters for the current digit.
        #   - Backtrack by appending the current letter to the current combination
        # NOTE: Here it is known that the current combination is not the same length
        # as the input string, so the current combination is not complete.
        for letters in digit_to_letters[digits[i]]:
            dfs(i + 1, current_string + letters)

    # Call the depth-first search helper function to generate all combinations
    # NOTE: An empty string is represented by an empty list
    if digits:
        dfs(0, "")

    # Return the list of combinations
    return combinations
