"""
Cracking the Coding Interview: 1.4

Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
You can ignore casing and non-letter characters

Example:
Input:  Tact Coa
Output: True (permutations: "taco cat", "atco cta", "etc.)
"""


# Algorithms Used: HashMap
# Time Complexity: O(n)
# Memory Complexity: O(1)
def palindromePermutation(chars: str):
    # Create a hash map where the key is the charater from the input string
    # and the value will be its frequency in the input string
    wordCountMap = {}

    # Count the number of occurrances for each letter character in the input string
    for char in chars:
        if isLetter(char):
            wordCountMap[char.lower()] = wordCountMap.get(char.lower(), 0) + 1

    # If multiple characters have an odd frequency it cannot be a palindrome
    for freq in wordCountMap.values():
        oddCountFound = False

        if freq % 2 == 1:
            if oddCountFound:
                return False
    
            oddCountFound = True

    return True
 

# Helper Function:
# Checks ascii value to determine if the character is a letter
def isLetter(c):
    return (
            (ord('A') <= ord(c) <= ord('Z')) or
            (ord('a') <= ord(c) <= ord('z')) 
           )
