"""
What is Big O?
    + Way to measure how the code will perform in time as the input size becomes larger
        - Worst case runtim

Big-O Order:
    O(1) < O(logn) < O(sqrt(n)) < O(n) < O(nlog(n)) < O(n^2) < O(n^3) < O(2^n) < O(n!) 
"""


"""
0(1)
    + Constant Time
    + No matter how much the input size grows the runtime remains the same
    + Most efficient algorithms
"""
def bigO1():
    # Array
    nums = [1, 2, 3]
    nums.append(4)    # push to end
    nums.pop()        # pop from end
    nums[0]           # lookup
    nums[1]
    nums[2]

    # HashMap / Set
    hashMap = {}
    hashMap["key"] = 10     # insert
    print("key" in hashMap) # lookup
    print(hashMap["key"])   # lookup
    hashMap.pop("key")      # remove


"""
O(n)
    + Linear Time
    + As the input size grows, the runtime will grow proportionately
"""
def bigOn():
    nums = [1, 2, 3]
    sum(nums)           # sum of array
    for n in nums:      # looping
        print(n)

    nums.insert(1, 100) # insert middle
    nums.remove(100)    # remove middle
    print(100 in nums)  # search

    import heapq
    heapq.heapify(nums) # build heap

    # sometimes even nested loops can be O(n)
    # (e.g. monotonic stack or sliding window)


"""
O(n^2)
"""
def bigOnpow2():
    # Traverse a square grid
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in range(len(nums)):
        for j in range(len(nums[i])): 
            print(nums[i][j])

    # Get every pair of elements in array
    nums = [1, 2, 3]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(nums[i], nums[j])

    # Insertion sort (insert in middle n times -> n^2)


"""
O(n * m)
    + Two-dimensional matrix that is not a square
        + n = rows
        + m = columns
"""
def bigOnm():
    # Traverse a square grid
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in range(len(nums)):
        for j in range(len(nums[i])): 
            print(nums[i][j])

    # Get every pair of elements in array
    nums = [1, 2, 3]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(nums[i], nums[j])

    # Insertion sort (insert in middle n times -> n^2)


"""
O(n^3)
"""
def bigOnpow3():
    # Get every triplet of elements in array
    nums = [1, 2, 3]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                print(nums[i], nums[j], nums[k])


"""
O(log(n))
 + Binary Search
 + On every iteration of the loop, half of the input data is removed
 + Grows slowly, good for larger datasets
"""
def bigOlogn():
    # Binary search
    nums = [1, 2, 3, 4, 5]
    target = 6
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if target < nums[m]:
            r = m - 1
        elif target > nums[m]:
            l = m + 1
        else:
            print(m)
            break

    # Binary Search on BST
    def search(root, target):
        if not root:
            return False
        if target < root.val:
            return search(root.left, target)
        elif target > root.val:
            return search(root.right, target)
        else: 
            return True

    # Heap Push and Pop
    import heapq
    minHeap = []
    heapq.heappush(minHeap, 5)
    heapq.heappop(minHeap)


"""
O(nlog(n))
    + Slightly less efficient than 0(n)
    + Sorting algorithms
"""
def bigOnlogn():
    # HeapSort
    import heapq
    nums = [1, 2, 3, 4, 5]
    heapq.heapify(nums)     # O(n)
    while nums:
        heapq.heappop(nums) # O(logn)

    # MergeSort (and most built-in sorting functions)


"""
O(2^n)
    + Recursion
        - Fibonacci
"""
def bigO2pown():
    # Recursion, tree height n, two branches
    def recursion(i, nums):
        if i == len(nums):
            return 0
        branch1 = recursion(i + 1, nums)
        branch2 = recursion(i + 2, nums)


"""
O(c^n)
"""
def bigOcpown():
    # c branches, where c is sometimes n.
    def recursion(i, nums, c):
        if i == len(nums):
            return 0
        
        for j in range(i, i + c):
            branch = recursion(j + 1, nums)


"""
O(sqrt(n))
"""
def bigOsqrtn():
    # Get all factors of n
    import math
    n = 12
    factors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)


"""
O(n!)
    - Rare
    - Very inefficient
"""
# Permutations
# Travelling Salesman Problem
