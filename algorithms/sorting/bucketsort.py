"""
What is Bucket Sort?
    - Bucket Sort is a sorting technique that sorts the elements by first
      dividing the elements into several groups called buckets
    - The elements inside each bucket are sorted using any of the suitable
      sorting algorithms or recursively calling the same algorithm

https://www.youtube.com/watch?v=VuXbEb5ywrU
"""

from typing import List


def bucketSort(nums: List[int]) -> List[int]:
    # Initialize an empty bucket
    bucket = []

    # Add each index from the input array into the bucket array
    # and initialize a list for each bucket element
    for i in range(len(nums)):
        bucket.append(i)
        bucket[i] = []
    
    # Iterate through input list
    # Define range for index in bucket array
    # Append every element falling into bucket list
    for j in nums:
        index = int(10 * j)

        bucket[index].append(j)

    # Sort each individual bucket
    for k in range(len(nums)):
        bucket[k] = sorted(bucket[k])


    # Iterate through input array
    # Add each element from bucket to the output list
    # Concatentate all buckets into the output array
    a = 0
    for b in range(len(nums)):
        for c in range(len(bucket[b])):
            nums[a] = bucket[b][c]
            a += 1

    return nums


l1 = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print(bucketSort(l1))
