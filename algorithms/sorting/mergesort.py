""""
Merge Sort
    - Divide-and-conqer algorithm
    - Breaks a dataset into individual pieces and merges them
    - Uses recursion to operate on datasets
    - Performs well on large sets of data
    - Time Complexity: O(nlog(n))
    - Memory Complexity: O(n)
"""

from typing import List


def mergesort(nums: List[int]):

    if len(nums) > 1:

        # Find the middle index and then the left and right portions of the array
        m = len(nums) // 2
        l = nums[:m]
        r = nums[m:]

        # Recursively break down the left and right portions of the array until
        # both or either array is a single element. This will ensure the primary
        # condition (len(nums) > 1) is satisfied, thus moving onto the next process
        mergesort(l)
        mergesort(r)

        # Now began merge sort
        i = 0 # Index into the left array
        j = 0 # Index into the right array
        k = 0 # Index into the merged array

        # Iterate through left and right array WHILE BOTH have content
        # Compare the current index value of the two arrays to see which is the
        # smaller and insert that value back into the original input list
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                nums[k] = l[i]
                i += 1
            else:
                nums[k] = r[j]
                j += 1
            k += 1

        # If LEFT-ONLY still has content, add them
        while i < len(l):
            nums[k] = l[i]
            i += 1
            k += 1

        # If RIGHT-ONLY still has content, add them
        while j < len(r):
            nums[k] = r[j]
            j += 1
            k += 1
