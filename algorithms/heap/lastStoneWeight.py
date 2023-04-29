"""
https://leetcode.com/problems/last-stone-weight/

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones.

On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y.

The result of this smash is:
    * If x == y, both stones are destroyed, and
    * If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Example 1:
    * Input: stones = [2,7,4,1,8,1]
    * Output: 1
    * Explanation: 
        - We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
        - we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
        - we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
        - we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1
 
Constraints:
    * 1 <= stones.length <= 30
    * 1 <= stones[i] <= 1000
"""

import heapq
from typing import List


# Algorithm Used: Max Heap
# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
def lastStoneWeight(stones: List[int]) -> int:
    # Convert the stones to negative values to create a max heap
    stones = [-stone for stone in stones]

    # Create a max heap from the stones (Time Complexity: O(n))
    heapq.heapify(stones)

    # While there are more than one stone in the heap
    # Remove the two largest stones and add the difference back to the heap
    # Return the last stone in the heap
    while len(stones) > 1:
        # Note using abs() is used since the stones are negative to represent a max heap
        first, second = abs(heapq.heappop(stones)), abs(heapq.heappop(stones))
        if second < first:
            heapq.heappush(stones, (first - second) * -1)

    # Return the last stone in the heap if it exists
    # Otherwise, return 0. This handles the case where there are no stones in the heap,
    # meaning that all stones were destroyed.
    return abs(stones[0]) if stones else 0
