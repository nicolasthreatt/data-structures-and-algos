"""
https://www.lintcode.com/problem/659/

Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example 1
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation: One possible encode method is: "lint:;code:;love:;you"

Example 2
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation: One possible encode method is: "we:;say:;:::;yes"
"""

from typing import List


# Time Complexity: O(n)
def encode(strs) -> str:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    # Initialize an empty string to encode the input list of strings
    new_str = ""

    # Iterate through input list of strings
    for s in strs:
        # Encode input string by adding its length and a special character
        # deliminter before the actual string. This help with decoding.
        new_str += str(len(s)) + "#" + s

    return new_str


# Time Complexity: O(n)
def decode(str) -> List:
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    new_list = []

    i = 0
    # Index through input string
    while i < len(str):
        # Determine the length of the list string. Remember from encode()
        # that the first markings of a new string is its length following 
        # by the special character deliminter.
        j = i
        while str[j] != "#":
            j += 1
        
        # NOTE:
        # my_list = ["1", "2", "3", "4", "5"]
        # int(my_list[0:1]) = 1
        # int(my_list[0:2]) = 12
        length = int(str[i:j])

        # From encode we know that a new string start one position AFTER the 
        # special character deliminter
        new_list.append(str[j + 1:j + 1 + length])

        # Update the index PAST the current decoded input string
        i = j + 1 + length

    return new_list
