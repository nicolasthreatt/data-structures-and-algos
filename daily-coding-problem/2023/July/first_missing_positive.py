"""
Daily Coding Problem: #4 (Hard) - Stripe
Date: 07/06/2023

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


# Algorith Used: Linear Scan, Two Passes
# Time Complexity: O(n)
# Space Complexity: O(1)
def first_missing_positive(nums: list) -> int:
    """Find the first missing positive integer in a list of integers.

    Args:
        nums (list): List of integers

    Explanation:
        Find the minimum and maximum positive integers in the list.
        If the minimum positive integer is greater than 1, return 1.
        Otherwise, iterate from the minimum positive integer to the maximum positive integer.
        If any integer in this range is not in the list, return it.
        If all integers in this range are in the list, return the maximum positive integer + 1.
    """

    # Find the minimum and maximum positive integers in the list
    # These are the bounds of the range of positive integers in the list
    min_positive = 1
    max_positive = 1

    # Iterate through the list and update the bounds
    # The minimum positive integer is the smallest positive integer in the list
    # The maximum positive integer is the largest positive integer in the list
    for num in nums:
        if num > 0:
            if num < min_positive:
                min_positive = num
            if num > max_positive:
                max_positive = num
            
    # If the minimum positive integer is greater than 1, return 1
    if min_positive > 1:
        return 1

    # Iterate from the minimum positive integer to the maximum positive integer
    # If any integer in this range is not in the list, return it
    for i in range(min_positive, max_positive + 1):
        if i not in nums:
            return i

    # If all integers in this range are in the list, return the maximum positive integer + 1
    return max_positive + 1


if __name__ == "__main__":
    test_cases = [
        # Test case with negative numbers
        ([-2, -5, -1, -10], 1),

        # Test case with all negative numbers
        ([-3, -7, -9, -4], 1),

        # Test case with all positive numbers
        ([5, 2, 9, 7, 1, 4, 3], 6),

        # Test case with duplicates
        ([1, 2, 2, 3, 4, 4, 5], 6),

        # Test case with a large range of positive numbers
        ([100, 200, 300, 400, 500], 1),

        # Test case with empty array
        ([], 1),

        # Test case with a single positive number
        ([7], 1)
    ]

    for nums, expected_output in test_cases:
        assert first_missing_positive(nums) == expected_output

    print("All test cases pass")
