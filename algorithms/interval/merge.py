"""
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

(0,8),(8,10) would merge to (0,10)

Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    * 1 <= intervals.length <= 10^4
    * intervals[i].length == 2
    * 0 <= starti <= endi <= 10^4
"""

from typing import List


# Algorithm Used: Sorting, Intervals
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def merge(intervals: List[List[int]]) -> List[List[int]]:
    # Sort the intervals by their start value (nlogn)
    intervals.sort(key=lambda i: i[0])

    # Create a new list to store the merged intervals
    # Add the first interval to the list of merged intervals
    merged_intervals = [intervals[0]]

    # Iterate through the sorted intervals
    for start, end in intervals[1:]:
        # Get the end value of the last merged interval
        last_end = merged_intervals[-1][1]

        # Check if the current interval overlaps with the last merged interval
        if start <= last_end:  # overlapping
            # Update the end value of the last merged interval to the maximum of
            # the current interval's end value and the last merged interval's end value
            merged_intervals[-1][1] = max(last_end, end)
        else:  # nonoverlapping
            # Add the current interval to the list of merged intervals
            merged_intervals.append([start, end])

    # Return the list of merged intervals
    return merged_intervals
