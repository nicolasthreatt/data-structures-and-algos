"""
Approaching Fibonacci - Numerator Interview

The Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1
    F(n) = F(n − 1) + F(n − 2), for n > 1.

Given an array of integers arr, define S as the sum of all elements in the array.

Your task is to determine the smallest non-negative integer that can be added to S
so that the resulting value is the next Fibonacci number greater than or equal to S.

Return the smallest integer that must be added.

Example 1:
    Input: arr = [15, 1, 3]
    Output: 2
    Explanation:
        Sum of array = 15 + 1 + 3 = 19
        The next Fibonacci number ≥ 19 is 21
        21 − 19 = 2

Example 2:
    Input: arr = [1, 2, 3]
    Output: 2
    Explanation:
        Sum of array = 6
        The next Fibonacci number ≥ 6 is 8
        8 − 6 = 2

Example 3:
    Input: arr = [0, 0, 0]
    Output: 0
    Explanation:
        Sum of array = 0
        0 is already a Fibonacci number

Constraints:
    * 1 <= arr.length <= 100
    * -10^4 <= arr[i] <= 10^4
"""


class ApproachingFibonacci:

    # Algorithm(s) Used: Dynammic Programming, Fibonacci Sequence
    # Time Complexity: O(log(F)), where F is the size of the NEXT Fibonacci number
    # Space Complexity: O(1)
    def approachingFibonacciI(self, arr: list) -> int:
        a, b = 0, 1  # Base Cases
    
        total_sum = sum(arr)

        # Handle case where total_sum is 0 (the smallest Fibonacci >= 0 is 0)
        if (a >= total_sum):
            return a - total_sum

        # Generate Fibonacci numbers until we reach or exceed total_sum
        while b < total_sum:
            a, b = b, a + b

        return b - total_sum


if __name__ == "__main__":
    Solution = ApproachingFibonacci()

    test_cases = [
        ([5, 2, 1], 0),
        ([1, 20, 2, 5], 6),
        ([15, 1, 3], 2),
        ([1], 0),
        ([2], 0),
        ([4], 1),
        ([0, 0], 0),
        ([7, 7, 7], 0),
        ([10, 10], 1),
        ([34], 0),
    ]

    functions = [
        Solution.approachingFibonacciI,
    ]

    for func in functions:
        for arr, expected in test_cases:
            assert func(arr) == expected
