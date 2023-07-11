"""
Daily Coding Problem: #9 (Hard) - Airbnb
Date: 07/11/2023

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example:
    - [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
    - [5, 1, 1, 5] should return 10, since we pick 5 and 5.
"""


# Algorith Used: 1-D Dynamic Programming, Buttom-Up
# Time Complexity: O(n)
# Space Complexity: O(1)
def largest_sum_non_adjacent(nums: list) -> int:
    # Initialize the largest sum of non-adjacent numbers 2 indices ago, 1 index ago, and at the current index
    largest_sum = 0
    largest_sum_2_indices_ago = 0
    largest_sum_1_index_ago = 0

    # Iterate through the list
    for num in nums:
        # Update the largest sum of non-adjacent numbers
        # At each iteration, the largest sum of non-adjacent numbers is the maximum of:
        #     - The sum of the current number and the largest sum of non-adjacent numbers 2 indices ago
        #     - The largest sum of non-adjacent numbers 1 index ago
        largest_sum = max(num + largest_sum_2_indices_ago, largest_sum_1_index_ago)

        # Update the largest sum of non-adjacent numbers 2 indices ago
        largest_sum_2_indices_ago = largest_sum_1_index_ago

        # Update the largest sum of non-adjacent numbers 1 index ago
        largest_sum_1_index_ago = largest_sum

    # Return the largest sum of non-adjacent numbers
    return largest_sum


if __name__ == '__main__':
    assert largest_sum_non_adjacent([2, 4, 6, 2, 5]) == 13
    assert largest_sum_non_adjacent([5, 1, 1, 5]) == 10
    assert largest_sum_non_adjacent([5, 1, 1, 1, 5, 1, 5]) == 16
    print('Passed all tests.')
