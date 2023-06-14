"""
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

(0,8),(8,10) is not conflict at 8

Example 1
    Input: intervals = [(0,30),(5,10),(15,20)]
    Output: false
    Explanation: (0,30), (5,10) and (0,30),(15,20) will conflict

Example 2
    Input: intervals = [(5,8),(9,15)]
    Output: true
    Explanation: Two times will not conflict 

Constraints:
    * The number of meeting time intervals will not exceed 100000.
    * The interval's start time is stored in the first element of the interval array.
    * The interval's end time is stored in the second element of the interval array.
"""

from typing import List

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

# Algorithm Used: Sorting, Intervals
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
def canAttendMeetings(intervals: List[List[int]]) -> bool:
    # Sort the intervals by their start time
    intervals.sort(key = lambda i : i.start)

    # Iterate through the intervals
    # Keep track of the previous interval and the current interval
    # If the previous interval's end time is greater than the current interval's start time,
    # then the intervals conflict so return False
    for i in range(1, len(intervals)):
        previous = intervals[i - 1]
        current = intervals[i]

        if previous.end > current.start:
            return False

    # If no conflicts were found, return True since it is possible to attend all meetings
    return True
