"""
https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z can be encoded into numbers using the following mapping:
    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using
the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
    Input: s = "12"
    Output: 2
    Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
    Input: s = "226"
    Output: 3
    Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
    Input: s = "06"
    Output: 0
    Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:
    * 1 <= s.length <= 100
    * s contains only digits and may contain leading zero(s).
"""


# Algorithm Used: Dynamic Programming, One-Dimensional, Buttom-Up
# Time Complexity: O(n)
# Memory Complexity: O(1)
def numDecodingsI(s: str) -> int:
    # Initialize variables for counting digits
    # NOTE ones_digit will be in sync with the current digit
    current_digit = 0  # Number of combinations that can be formed with the current digit
    ones_digit = 1  # Number of combinations that can be formed with the digit one position away
    twos_digit = 0  # Number of combinations that can be formed with the digit two positions away

    # Iterate through the string in reverse order
    # NOTE: Recall that ones_digit and twos_digit variables are initialized to 1 and 0 respectively
    for i in range(len(s) - 1, -1, -1):
        # Increment current digit count if the current character is not '0'
        # This is because characters '1' to '9' can be mapped to 'A' to 'I' respectively so
        # there is at least one combination that can be formed with the current digit
        if s[i] != "0":
            current_digit += ones_digit

        # Increment current digit count if the current and next characters form a valid two-digit number
        # This is because characters '10' to '26' can be mapped to 'J' to 'Z' respectively so
        # there are at least two combinations that can be formed with the current digit and next digit
        if (i + 1 < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
            current_digit += twos_digit

        # Update variables for the next iteration
        twos_digit = ones_digit  # Move the previous one_digit value to twos_digit
        ones_digit = current_digit  # Move the current_digit value to ones_digit
        current_digit = 0  # Reset the current_digit for the next iteration

    # Return the count of numbers that can be formed
    # NOTE: ones_digit is returned because it contains the count of numbers that can be formed since
    #       the ones_digit variable is in sync with the current digit.
    return ones_digit


# Algorithm Used: Dynamic Programming, One-Dimensional, Top-Down, DFS
# Time Complexity: O(n)
# Memory Complexity: O(n)
def numDecodingsII(s: str) -> int:
    # If string is empty, then would need to return 1
    # Will be used for base case in dfs helper function
    dp = {len(s): 1}

    def dfs(current_index: int) -> int:
        """
        Helper function that will be used to recursively find the number of ways to decode the string

        Args:
            current_index (int): The current index in the string

        Returns:
            int: The number of ways to decode the string starting at the current index
        """

        # BASE CASE (VALID CHAR)
        # If the current index is in the dp hash,
        # then the number of ways to decode the string starting at the current index has already been calculated.
        # Initially, the dp hash will only contain the number of ways to decode the string starting at the last index.
        if current_index in dp:
            return dp[current_index]

        # BASE CASE (INVALID CHAR)
        # If the current character is 0, then the current character is not valid.
        if s[current_index] == "0":
            return 0

        # RECURSIVE CASE
        # Here its assumed that the current character can be decoded by at least 1 one character
        num_decodings = dfs(current_index + 1)

        # If the next character is in bounds and both the current and next characters are valid
        # then the current character can be combined with the next character meaning
        # that there are 2 characters to decode the string.
        # For example, if the current character is 1 and the next character is 2,
        # then the current character can be combined with the next character to form 12.
        if current_index + 1 < len(s) and (
            s[current_index] == "1" or (s[current_index] == "2" and s[current_index + 1] in "0123456")
        ):
            num_decodings += dfs(current_index + 2)

        # Store the number of ways to decode the string starting at the current index
        dp[current_index] = num_decodings

        # Return the number of ways to decode the string starting at the current index
        return num_decodings

    # Return the number of ways to decode the string starting at index 0
    return dfs(0)
