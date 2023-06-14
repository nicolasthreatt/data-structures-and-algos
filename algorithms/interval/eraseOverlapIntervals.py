"""
https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

(0,8),(8,10) would merge to (0,10)

Example 1:
    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
    Input: intervals = [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
    Input: intervals = [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
    * 1 <= intervals.length <= 2 * 10^4
    * intervals[i].length == 2
    * -2 * 10^4 <= starti < endi <= 2 * 10^4
"""

from typing import List


# Algorithm Used: Sorting, Intervals, Greedy
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    # Sort the intervals by their start value (nlogn)
    intervals.sort()

    # Initialize the number of intervals removed and the end value of the last merged interval (prev_end)
    removed = 0
    prev_end = intervals[0][1]

    # Iterate through the sorted intervals
    for curr_start, curr_end in intervals[1:]:
        # If the current interval does not overlap with the last merged interval,
        # update the end value of the last merged interval to the end value of the current interval.
        # This is because the current interval is the next nonoverlapping interval.
        if curr_start >= prev_end:  # nonoverlapping
            prev_end = end
        # If the intervals overlap, increment the number of intervals removed and update
        # the end value of the last merged interval to the minimum of the current interval's
        # end value and the last merged interval's end value.
        # This is because the current interval is overlapping with the last merged interval
        # and need to ensure for the next iteration that the current interval is not overlapping.
        else:
            removed += 1
            prev_end = min(prev_end, curr_end)

    # Return the number of intervals removed
    return removed
