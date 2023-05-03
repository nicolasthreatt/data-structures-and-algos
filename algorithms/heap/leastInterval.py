"""
https://leetcode.com/problems/task-scheduler/

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
Tasks could be done in any order. Each task is done in one unit of time.
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

Constraints:
    * 1 <= task.length <= 10^4
    * tasks[i] is upper-case English letter.
    * The integer n is in the range [0, 100].
"""

import heapq
from typing import List
from collections import deque, Counter


# Algorithm Used: Max Heap, Queue
# Time Complexity: O(n), where n is the number of tasks
# Space Complexity: O(n), where n is the number of tasks
def leastInterval(tasks: List[str], n: int) -> int:
    # Initialize a counter to store the number of times each task appears.
    count = Counter(tasks)

    # Initialize a max heap to store the tasks with the most occurances.
    # Note the tasks are stored as negative values to create a max heap.
    maxHeap = [-cnt for cnt in count.values()]  # O(n)
    heapq.heapify(maxHeap)  # O(log(n)

    # Initialize a variable to keep track of the time.
    time = 0

    # Create a queue to store the tasks that are waiting to be processed.
    queue = deque()  # [-cnt, idleTime]

    # While there are tasks in the max heap or queue:
    #   - Increment the time for each iteration.
    #   - If there are tasks in the max heap, pop the task with the most occurances and add it to the queue.
    #   - If the queue is not empty and the idle time is equal to the current time, add the task back to the max heap.
    #     This means that the task is ready to be processed again.
    while maxHeap or queue:  # O(n)
        time += 1

        if maxHeap:
            # Note that cnt will represent the number of occurances of the current largest task
            # and will be negative since the tasks are stored as negative values in the max heap.
            # Add 1 to account for the current task being processed. (i.e. 1 + (-3)).
            cnt = 1 + heapq.heappop(maxHeap)  # O(log(n))
            if cnt:  # Once reaches 0, then a task has been processed.
                queue.append([-cnt, time + n])

        # Note that the queue stores the count of the task as the first element and the idle time as the second element.
        if queue and queue[0][1] == time:
            heapq.heappush(maxHeap, queue.popleft()[0])

    # Return the time it took to process all the tasks.
    return time
