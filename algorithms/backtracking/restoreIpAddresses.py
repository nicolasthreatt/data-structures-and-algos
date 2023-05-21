"""
https://leetcode.com/problems/restore-ip-addresses/

A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s.
You are not allowed to reorder or remove any digits in s.
You may return the valid IP addresses in any order.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
    * 1 <= s.length <= 20
    * s consists of digits only.
"""

from typing import List


# Algorithm Used: Backtracking, Recursion
# Time Complexity: (3^n), but if n is 12 or greater, it is O(1)
# Space Complexity: (3^n), but if n is 12 or greater, it is O(1)
def restoreIpAddresses(s: str) -> List[str]:
    ip_addresses = []

    # CHECKPOINT:
    #   - If the length of the input string is less than 4 or greater than 12,
    #     then an ip address cannot be formed so return the list of IP addresses.
    if len(s) < 4 or len(s) > 12:
        return ip_addresses

    def backtrack(i: int, dots: int, current_ip: str):
        # BASE CASE (SUCCESS):
        #   - If the number of dots is 4 and the index has reached the end of the input string,
        #     then the current IP address is valid so append it to the list of IP addresses.
        if dots == 4 and i == len(s):
            # Remove the last dot from current IP address before appending to list of IP addresses.
            ip_addresses.append(current_ip[:-1])
            return

        # BASE CASE (FAILURE):
        #   - If the number of dots is greater than 4, then the current IP address is invalid so return.
        if dots > 4:
            return

        # RECURSIVE CASE:
        #   - Iterate through the range of numbers from the current index to the current index + 3.
        #     If the current index + 3 is greater than the length of the input string,
        #     then the stop index is the length of the input string.
        #     This is to ensure that the current index does not go out of bounds.
        #   - If the current number is less than 255 and the current number is not 0 or
        #     the current number is 0 and the current index is the same as the stop index,
        #     then append the current number to the current IP address and recursively call the function.
        for j in range(i, min(i + 3, len(s))):
            # LEADING ZERO CHECK
            if int(s[i : j + 1]) <= 255 and (i == j or s[i] != "0"):
                backtrack(j + 1, dots + 1, current_ip + s[i : j + 1] + ".")

    # Call the helper function to get all IP addresses
    backtrack(0, 0, "")

    # Return the list of IP addresses
    return ip_addresses
