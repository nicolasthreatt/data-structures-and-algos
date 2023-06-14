"""
https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

(0,8),(8,10) would merge to (0,10)

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
    * 0 <= intervals.length <= 10^4
    * intervals[i].length == 2
    * 0 <= starti <= endi <= 10^5
    * intervals is sorted by starti in ascending order.
    * newInterval.length == 2
    * 0 <= start <= end <= 10^5
"""

from typing import List


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


# Algorithm Used: Sorting, Intervals
# Time Complexity: O(n)
# Space Complexity: O(n)
def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    # If the list of intervals is empty, then immediately return the new interval since nothing to merge with
    if not intervals:
        return [new_interval]

    # Initialize a list to store the merged intervals
    merged_intervals = []

    # Get the start and end values of the new interval
    new_start, new_end = new_interval

    # Iterate through the list of intervals
    #     + Check for nonoverlapping intervals
    #        - If the new interval's end time is less than the current interval's start time,
    #          then the new interval is nonoverlapping and should be inserted BEFORE the current interval
    #        - If the new interval's start time is greater than the current interval's end time,
    #          then the new interval is nonoverlapping and should be inserted AFTER the current interval
    #     + Check for overlapping intervals
    #        - If the new interval's end time is greater than the current interval's end time,
    #          then the new interval's end time is the current interval's end time
    for i in range(len(intervals)):
        current_start, current_end = intervals[i]

        if new_end < current_start:  # nonoverlapping (new end time < current start time)
            merged_intervals.append(new_interval)
            return merged_intervals + intervals[i:]
        elif new_end > current_end:  # nonoverlapping (new start time > current end time)
            merged_intervals.append(intervals[i])
        else:  # overlapping (new end time > current end time)
            new_interval = [min(new_start, current_start), max(new_end, current_end)]

    # Add the new interval to the list of merged intervals and return the list of merged intervals
    # This is for cases where new interval is nonoverlapping and should be inserted at the end of list of intervals
    return merged_intervals.append(new_interval)
