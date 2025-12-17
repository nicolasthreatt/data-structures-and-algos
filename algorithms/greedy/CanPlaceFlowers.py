"""
Can Place Flowers
https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some are not.

However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed
without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

Constraints:
    * 1 <= flowerbed.length <= 2 * 104
    * flowerbed[i] is 0 or 1.
    * There are no two adjacent flowers in flowerbed.
    * 0 <= n <= flowerbed.length
"""

from typing import List


class CanPlaceFlowers:

    # Algorithm(s) Used: Greedy, Padding
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def canPlaceFlowersI(self, flowerbed: List[int], n: int) -> bool:
        flowers = [0] + flowerbed + [0]

        # Skip First and Last Elements (Modified 0's)
        for i in range(1, len(flowers) - 1):
            left_plot_empty = flowers[i - 1]
            curr_plot_empty = flowers[i]
            right_plot_empty = flowers[i + 1]

            # Greedy Choice - Plant Flower
            if left_plot_empty == curr_plot_empty == right_plot_empty == 0:
                n -= 1  # Local Optimal Choice
                flowers[i] = 1
        
        return n <= 0  # Global Optimal Solution

    # Algorithm(s) Used: Greedy
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def canPlaceFlowersII(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            left_plot_empty = (i == 0) or (flowerbed[i - 1] == 0)  # [0, 0, 1]
            curr_plot_empty = flowerbed[i] == 0  # [0, 0, 0]
            right_plot_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)  # [1, 0, 0]

            # Greedy Choice - Plant Flower
            if left_plot_empty and curr_plot_empty and right_plot_empty:
                n -= 1  # Local Optimal Choice
                flowerbed[i] = 1
        
        return n <= 0  # Global Optimal Solution


if __name__ == "__main__":
    Solution = CanPlaceFlowers()

    # (flowerbed, n, expected)
    test_cases = [
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([0], 1, True),
        ([0], 0, True),
        ([1], 1, False),
        ([0, 0, 0, 0, 0], 3, True),
        ([0, 0, 1, 0, 0], 2, True),
        ([0, 0, 1, 0, 0], 3, False),
        ([1, 0, 0, 0, 0, 1], 2, False),
        ([0, 0, 0], 2, True),
    ]

    funcs = [
        Solution.canPlaceFlowersI,
        Solution.canPlaceFlowersII,
    ]

    for func in funcs:
        for flowerbed, n, expected in test_cases:
            result = func(flowerbed.copy(), n)
            assert result == expected
