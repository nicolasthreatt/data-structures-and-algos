"""
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites
where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.

Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
    So it is impossible.

Constraints:
    * 1 <= numCourses <= 2000
    * 0 <= prerequisites.length <= 5000
    * prerequisites[i].length == 2
    * 0 <= ai, bi < numCourses
    * All the pairs prerequisites[i] are unique.
"""

from typing import List


# Algorithm Used: Graph, Depth First Search
# Time Complexity: O(n + p), where n is the number of courses and p is the number of prerequisites
# Space Complexity: O(n + p), O(n + p), where n is the number of courses and p is the number of prerequisites
def canFinishI(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Map each course to an empty list of prerequisites (course -> [])
    prerequisitesMap = {course: [] for course in range(numCourses)}

    # Iterate through the prerequisites and map each course to its prerequisites
    # Key: course
    # Value: list of prerequisites (other courses that must be taken before the course)
    for course, prereq in prerequisites:
        prerequisitesMap[course].append(prereq)

    # Initialize a set to store the visited courses.
    # This is used to detect cycles in the graph.
    visitedSet = set()

    def dfs(course: int) -> bool:
        """Depth First Search helper function to traverse the graph.

        If the course has already been visited, then there is a cycle in the graph.
        If the course has no prerequisites, then it can be finished.
        Otherwise, recursively call dfs on all the prerequisites of the course.
        If any of the prerequisites cannot be finished, then the course cannot be finished.
        If all the prerequisites can be finished, then the course can be finished.

        Args:
            course (int): The current course to traverse.

        Returns:
            bool: True if the course can be finished, False otherwise.
        """
        # BASE CASE (INVALID PATH)
        # If the course has already been visited, then there is a cycle in the graph.
        if course in visitedSet:
            return False

        # BASE CASE (VALID PATH)
        # If the course has no prerequisites, then it can be finished.
        if prerequisitesMap[course] == []:
            return True

        # Here, so far there is a valid path to finish the course.
        # Add the course to the visited set.
        visitedSet.add(course)

        # Recursively call dfs on all the prerequisites of the course.
        # If any of the prerequisites cannot be finished, then the course cannot be finished.
        for prereq in prerequisitesMap[course]:
            if not dfs(prereq):
                return False

        # Here, all the prerequisites can be finished.
        # Remove the course from the visited set and set its prerequisites to an empty list.
        # This will reset the prerequisites of the course for the next dfs call.
        visitedSet.remove(course)
        prerequisitesMap[course] = []

        # Return True to indicate that the course can be finished.
        return True

    # For each course, call dfs on it, which will look for a valid path to finish the course.
    # If any of the courses cannot be finished, then return False.
    for course in range(numCourses):
        if not dfs(course):
            return False

    # All the courses can be finished, so return True.
    return True


# Algorithm Used: Graph, Breadth First Search
# Time Complexity: O(V+E), where V is the number of vertices and E is the number of edges
# Space Complexity: O(V+E), where V is the number of vertices and E is the number of edges
def canFinishII(numCourses: int, prerequisites: List[List[int]]) -> bool:
    pass
