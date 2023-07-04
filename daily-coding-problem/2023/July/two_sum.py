"""
Daily Coding Problem: #1 (Easy) - Google
Date: 07/03/2023

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

# Algorith Used: Two Pointers
# Time Complexity: O(n log n), where n is the length of the list
# Space Complexity: O(1), where n is the length of the list
def two_sumI(nums: list, k: int) -> bool:
    # Sort list (O(n log n)
    nums.sort()

    # Initialize left and right pointers
    l, r = 0, len(nums) - 1

    # Iterate through list until pointers meet (O(log n))
    # If sum of pointers is less than k, increment left pointer
    # If sum of pointers is greater than k, decrement right pointer
    # If sum of pointers is equal to k, return True
    while l < r:
        if nums[l] + nums[r] < k:
            l += 1
        elif nums[l] + nums[r] > k:
            r -= 1
        else:
            return True

    # Return False if pointers do not meet, 
    # which means that no two numbers add up to k
    return False

# Algorith Used: Two Pointers
# Time Complexity: O(n), where n is the length of the list
# Space Complexity: O(1)
def two_sumII(nums: list, k: int) -> bool:
    # Initialize a set to store the unique numbers in the input list
    seen = set()

    # Iterate through list
    # If k - num is in the set, return True
    # Otherwise, add num to the set
    for num in nums:
        if k - num in seen:
            return True
        seen.add(num)

    # Return False if no two numbers add up to k
    return False


if __name__ == "__main__":

    # Example
    nums = [10, 15, 3, 7]
    k = 17
    assert two_sumI(nums, k) == True

    # Example
    nums = [10, 15, 3, 7]
    k = 17
    assert two_sumII(nums, k) == True
