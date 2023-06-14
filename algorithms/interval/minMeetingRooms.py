"""
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

(0,8),(8,10) is not conflict at 8

Example 1:
    Input: intervals = [(0,30),(5,10),(15,20)]
    Output: 2
    Explanation: We need two meeting rooms
                 room1: (0,30)
                 room2: (5,10),(15,20)

Example 2:
    Input: intervals = [(2,7)]
    Output: 1
    Explanation: Only need one meeting room

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

# Algorithm Used: Sorting, Two Pointers, Intervals
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def minMeetingRooms(intervals: List[List[int]]) -> int:
    # Initialize and sort the start and end arrays (nlogn)
    # These arrays will be used to keep track of the start and end times of the intervals.
    # A new room is needed if the start time of the current interval is less than the end time of the current interval.
   start = sorted([i.start for i in intervals])
   end = sorted([i.end for i in intervals])

    # Initialize the number of rooms needed and the current number of meetings
    rooms_needed, currennt_meetings = 0, 0

    # Initialize the start and end pointers (Two Pointers)
    s, e = 0, 0

    # Iterate through the intervals
    # If the start time of the current interval is less than the end time of the current interval,
    # then a new room is needed so increment the current number of meetings.
    # Otherwise, a room is no longer needed so increment the end pointer and decrement the current number of meetings.
    # Keep track of the maximum number of rooms needed.
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            currennt_meetings += 1
        else:
            e += 1
            currennt_meetings -= 1

        rooms_needed = max(rooms_needed, currennt_meetings)
    
    # Return the maximum number of rooms needed to attend all meetings
    return rooms_needed