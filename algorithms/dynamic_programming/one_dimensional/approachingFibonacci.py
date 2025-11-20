"""
Approaching Fibonacci - Numerator Interview

Have the function approachingFibonacci(arr) take the arr parameter,
which will be a list of integers, and determine the smallest positive
integer (including zero) that can be added to the array so that the
sum becomes the next closest Fibonacci number.

Example:
    arr = [15, 1, 3] → sum = 19 → next Fibonacci = 21 → answer = 2
"""


# Algorithm(s) Used: Dynammic Programming, Fibonacci Sequence
# Time Complexity: O(log F), where F is the size of the next Fibonacci number
# Space Complexity: O(1)
def approachingFibonacci(arr: list) -> int:
    total_sum = sum(arr)

    a, b = 0, 1

    # Handle case where total_sum is 0 (the smallest Fibonacci >= 0 is 0)
    if (a >= total_sum):
        return a - total_sum

    # Generate Fibonacci numbers until we reach or exceed total_sum
    while b < total_sum:
        a, b = b, a + b

    return b - total_sum


if __name__ == "__main__":
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

    for arr, expected in test_cases:
        result = approachingFibonacci(arr)
        assert result == expected
