"""
Course Schedule II
https://leetcode.com/problems/course-schedule-ii

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.

You are given an array prerequisites, where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: [0,1]
    Explanation:
        - There are a total of 2 courses to take.
        - To take course 1 you should have finished course 0.
        - So the correct course order is [0,1].

Example 2:
    Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]
    Explanation:
        - There are a total of 4 courses to take.
        - To take course 3 you should have finished both courses 1 and 2.
        - Both courses 1 and 2 should be taken after you finished course 0.
        - So one correct course order is [0,1,2,3].
        - Another correct ordering is [0,2,1,3].

Example 3:
    Input: numCourses = 1, prerequisites = []
    Output: [0]

Constraints:
    * 1 <= numCourses <= 2000
    * 0 <= prerequisites.length <= numCourses * (numCourses - 1)
    * prerequisites[i].length == 2
    * 0 <= ai, bi < numCourses
    * ai != bi
    * All the pairs [ai, bi] are distinct.
"""

from collections import defaultdict
from typing import List


# Algorith Used: Topological Sort, DFS
# Time Complexity: O(p + n), where p = prerequisites and n = numCourses
# Space Complexity: O(p + n), where p = prerequisites and n = numCourses
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]: 

    # Base Case: No prerequisites, so any order of all course is valid
    if not prerequisites:
        return [course for course in range(numCourses)]
    
    # Build adjacency list: course -> prerequisites
    course_prereqs = defaultdict(list)
    for course, prereq in prerequisites:
        course_prereqs[course].append(prereq)

    # visited = courses already have been fully processed (safe, no cycles)
    # cycle   = courses CURRENTLY in the recursion stack (used to detect cycles)
    visited, cycle = set(), set()

    # Stores final ordering of courses
    #   - Only adds a course after processing all the prerequisites
    #   - At the end, reversing this list gives a valid topological order
    topological_path = []

    def dfs(course: int) -> bool:
        # Base Case: Cycle detected (invalid topological_path)
        if course in cycle:
            return False
        
        # Base Case: Already processed (skip course)
        if course in visited:
            return True
        
        cycle.add(course)

        # Visit all prerequisites to ensure course is valid (no cycle)
        for prereq in course_prereqs[course]:
            if not dfs(prereq):
                return False
        
        cycle.remove(course)  # Backtrack

        visited.add(course)   # Mark current course as processed
        topological_path.append(course)   # Add to course order

        return True
    
    # Run DFS on all courses
    for course in range(numCourses):
        if not dfs(course):  # Cycle detected
            return []
    
    return topological_path


if __name__ == "__main__":
    numCourses, prerequisites = 2, [[1,0]]
    assert findOrder(numCourses, prerequisites) == [0,1]

    numCourses, prerequisites = 4, [[1,0],[2,0],[3,1],[3,2]]
    assert findOrder(numCourses, prerequisites) in ([0,1,2,3], [0,2,1,3])

    numCourses, prerequisites = 1, []
    assert findOrder(numCourses, prerequisites) == [0]
