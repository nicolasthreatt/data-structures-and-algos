"""
Prefix Sum:
    - Computes the running sum of an array
    - Useful when you want to retrieve the sum of a subarray ending at index i
    - Use when you need to query subarray sums in O(1) time

Example Problems:
    1. Range Sum Query
        - Given an array nums, answer multiple queries of the form sumRange(left, right)
        - Prefix sum allows each query to be answered in O(1)
    2. Subarray Sum Equals K
        - Count the number of subarrays whose sum equals k
        - Use prefix sums + hashmap to track previous sums
    3. Product of Array Except Self
        - Prefix sums concept extends to prefix products
        - Compute left and right products efficiently
    4. Continuous Subarray Sum
        - Determine if a subarray sum is a multiple of k
        - Prefix sums + modulo trick
    5. Running Sum of 1D Array
        - Basic prefix sum construction problem

Time Complexity:
    - Build the prefix array: O(n)
    - Range sum query: O(1)

Space Complexity:
    - O(n) to store prefix sums
    - Can be O(1) extra space if modifying the input array in-place

Use Cases:
    - Fast range sum queries
    - Subarray sum problems
    - Sliding window optimizations
    - Prefix products / prefix XOR variants
"""


class PrefixSum:
    def __init__(self, nums: list):
        self.nums = nums
        self.prefix = []  # prefix[i] = sum(nums[0..i])

        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def runningSum(self) -> list:
        """Returns the full prefix sum array."""
        return [] if not self.prefix else self.prefix[:]

    def rangeSum(self, left: int, right: int) -> int:
        """Returns sum of nums[left..right] in O(1)."""
		if not self.prefix:
			return 0

        right_sum = self.prefix[right]
        left_sum = self.prefix[left - 1] if left > 0 else 0
        return right_sum - left_sum

    def prefixSumAt(self, i: int) -> int:
        """Returns sum of nums[0..i]."""
        return 0 if not self.prefix else self.prefix[i]

    def sumFirstK(self, k: int) -> int:
        """Returns sum of first k elements (nums[0..k-1])."""
        return 0 if not self.prefix or k <= 0 else self.prefix[k - 1]

    def hasSubarrayWithSum(self, k: int) -> bool:
        """Returns True if there exists at least one subarray whose sum equals k."""
		if not self.prefix:
			return False

        seen = {0}
        curr_sum = 0

        for n in self.nums:
            curr_sum += n
            if curr_sum - k in seen:
                return True
            seen.add(curr_sum)

        return False

    def countSubarraysWithSum(self, k: int) -> int:
        """
        Counts number of subarrays whose sum equals k
        (Prefix sum + hashmap frequency)
        """
		if not self.prefix:
			return 0

        subarrays = 0
        curr_sum = 0
        freqs = {0: 1}

        for n in self.nums:
            curr_sum += n
            subarrays += freqs.get(curr_sum - k, 0)
            freqs[curr_sum] = freqs.get(curr_sum, 0) + 1

        return subarrays


if __name__ == "__main__":
    Solution = PrefixSum([1, 2, 3, 4, 5])

    # (left, right, expected_sum)
    range_sum_tests = [
        (0, 0, 1),
        (0, 2, 6),
        (1, 3, 9),
        (2, 4, 12),
        (0, 4, 15),
    ]
    for left, right, expected in range_sum_tests:
        result = Solution.rangeSum(left, right)
        assert result == expected

    # (k, expected_bool)
    has_subarray_tests = [
        (3, True),
        (9, True),
        (15, True),
        (20, False),
    ]
    for k, expected in has_subarray_tests:
        result = Solution.hasSubarrayWithSum(k)
        assert result == expected

    # (k, expected_count)
    count_subarray_tests = [
        (3, 2),
        (5, 2),
        (15, 1),
    ]
    for k, expected in count_subarray_tests:
        result = Solution.countSubarraysWithSum(k)
        assert result == expected
