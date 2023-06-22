"""
https://leetcode.com/problems/maximum-profit-in-job-scheduling/

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i],
obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays,
return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:
    Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
    Output: 120
    Explanation: The subset chosen is the first and fourth job. 
                 Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:
    Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
    Output: 150
    Explanation: The subset chosen is the first, fourth and fifth job. 
                 Profit obtained 150 = 20 + 70 + 60.

Example 3:
    Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
    Output: 6

Constraints:
    * 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
    * 1 <= startTime[i] < endTime[i] <= 10^9
    * 1 <= profit[i] <= 10^4
"""

from typing import List


# Algorithm: Dynamic Programming, Intervals
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def jobSchedulingI(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    n = len(startTime)

    jobs = list(zip(startTime, endTime, profit))

    jobs.sort()

    @cache
    def helper(i):
        if i == n:
            return 0

        j = i + 1
        while j < n and jobs[i][1] > jobs[j][0]:
            j += 1
        
        one = jobs[i + 2] + helper(j)
        two = helper(j + 1)

        return max(one, two)
    
    return helper(0)


# Algorithm: Max Heap, Intervals
# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
def jobSchedulingII(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    # Create a list of jobs
    jobs = list(zip(startTime, endTime, profit))

    # Sort the jobs by start time
    jobs.sort()

    # Create a min heap, which will store the jobs by end time
    heap = []

    # Create a variable to store the max profit
    max_profit = 0

    # Iterate through the jobs
    for start, end, profit in jobs: # O(n)
        # If the current job's start time is greater than the end time of the first job in the heap,
        # then we can pop the first job in the heap and add its profit to the current job's profit
        # because the first job in the heap has an end time that is less than the current job's start time.
        while heap and heap[0][0] <= start:
            max_profit = max(max_profit, heapq.heappop(heap)[-1]) # O(log(n))
        heapq.heappush(heap, (end, profit + max_profit)) # O(log(n))
    
    # Pop the remaining jobs in the heap and update the max profit
    while heap:
        max_profit = max(max_profit, heapq.heappop(heap)[-1])

    # Return the max profit
    return max_profit
