"""
https://leetcode.com/problems/n-th-tribonacci-number/

The Tribonacci sequence Tn is defined as follows:
    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:
    Input: n = 4
    Output: 4
    Explanation:
        T_3 = 0 + 1 + 1 = 2
        T_4 = 1 + 1 + 2 = 4

Example 2:
    Input: n = 25
    Output: 1389537

Constraints:
    * 0 <= n <= 37
    * The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""


# Algorithm Used: Recursion
# Time Complexity: O(n)
# Space Complexity: O(1)
def tribonacci(n: int) -> int:
    # Initialize the first three numbers of the Tribonacci sequence.
    # This is necessary because the Tribonacci sequence is defined as:
    #   T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
    # So, we need to initialize the first three numbers of the sequence
    # in order to calculate the next sequence.
    tribonacci_seq = [0, 1, 1]

    # If n is less than 3, return the nth number of the Tribonacci sequence.
    # NOTE: Above the first three numbers of the Tribonacci sequence.
    if n < 3:
        return tribonacci_seq[n]

    # Calculate the next number of the Tribonacci sequence until we reach the nth number.
    # The calculation is based on the definition of the Tribonacci sequence.
    for _ in range(3, n + 1):
        tribonacci_seq = [tribonacci_seq[1], tribonacci_seq[2], sum(tribonacci_seq)]

    # Return the nth number of the Tribonacci sequence, which is represented by
    # the last number in the sequence.
    return tribonacci_seq[-1]  # tribonacci_seq[-1] == tribonacci_seq[2]
