"""
Daily Coding Problem: #2 (Hard) - Uber
Date: 07/04/2023

Given an array of integers, return a new array such that
each element at index i of the new array is the product of
all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24].

If our input was [3, 2, 1],
the expected output would be [2, 3, 6].
"""


# Algorith Used: Linear Scan, Two Passes
# Time Complexity: O(n)
# Space Complexity: O(n)
def product_except_self(nums: list) -> list:
    # Generate a list of the prefix multipliers by scanning the list from left to right
    # The prefix multiplier of a number is the product of all the numbers to the left of it
    prefix = []
    for num in nums:
        if prefix:
            # Multiply the current number with the previous prefix multiplier
            prefix.append(prefix[-1] * num)
        else:
            # If it's the first number, the prefix multiplier is the number itself.
            # This is because there are no numbers to the left of it, so basically multiply it by 1.
            prefix.append(num)
    
    # Generate a list of the postfix multipliers by scanning the list from right to left
    # The postfix multiplier of a number is the product of all the numbers to the right of it
    postfix = []
    for num in reversed(nums):
        if postfix:
            # Multiply the current number with the previous postfix multiplier
            postfix.append(postfix[-1] * num)
        else:
            # If it's the last number, the postfix multiplier is the number itself
            # This is because there are no numbers to the right of it, so basically multiply it by 1.
            postfix.append(num)
    
    # Reverse the postfix list so that it's in the same order as the original list
    postfix = list(reversed(postfix))

    # Generate the output list
    product = []

    # For each number, multiply the prefix multiplier of the previous number with
    for i in range(len(nums)):
        if i == 0:
            # The product at index 0 is the postfix multiplier of the next number
            product.append(postfix[i + 1])
        elif i == len(nums) - 1:
            # The product at the last index is the prefix multiplier of the previous number
            product.append(prefix[i - 1])
        else:
            # Multiply the prefix multiplier of the previous number with
            # the postfix multiplier of the next number
            product.append(prefix[i - 1] * postfix[i + 1])

    return product

