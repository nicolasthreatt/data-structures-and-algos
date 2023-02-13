"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
NOTE: Binary search tress have run time complexity O(log(n))

Example 1:
- Input: nums1 = [1,3], nums2 = [2]
- Output: 2.00000
- Explanation: merged array = [1,2,3] and median is 2.

Example 2:
- Input: nums1 = [1,2], nums2 = [3,4]
- Output: 2.50000
- Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

from typing import List


# Binary Search - log(min(A, B))
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    # Make sure A is the smaller of the arrays
    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2    # A - Index of midpoint A
        j = half - i - 2    # B - Index of midpoint B (-1 for index offset and -1 for B's offeset)

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
    
        # Look for correction partition
        if Aleft <= Bright and Bleft <= Aright:

            # odd array size
            if total % 2:
                return min(Aright, Bright)
            
            # even arry rize
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else: # Bleft > Aright
            l = i + 1
