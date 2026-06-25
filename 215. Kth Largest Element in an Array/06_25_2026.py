# # submission: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/2046115008/
# # runtime: 107 ms (beats 19.42%), memory: 31.44 MB (beats 11.99%)
# # 9 min
# # solved using heap

# # TC: O(n log (n-k+1))
# # - iterating through all elements: O(n)
# # - each pushing and popping to/from heap: O(log (n-k+1))
# # SC: O(n-k+1) (heap size)

# # cf.) in terms of time complexity, n log k and n log (n-k+1) are the same since the range of k is [1, n].


# # bc the problem explicitly asks not to use sorting, i directly considered using a heap data structure. i first tried to keep the heap with size k, but couldn't think of the correct solution while simulating on the test cases, lol (actually, it's more intuitive and straightfoward to keep the size of k). after a while, i noticed i can instead keep the size of n-k+1, and solved that way.

# # a simpler heap solution can be found in the "LeetCode Editorial's Approach 2: Min-Heap" section.

# cf.) there are several solutions for this problem. they are listed below, and the order is based on the what would be expected, safer, and eaiser to implement during the coding interview:
# 1. heap of size k: safest, clean, and deterministic O(n log k) time
# 2. quick select: best average time O(n), but more bug-prone and worst-case O(n^2) time
# 3. counting sort: good for this problem since he value range is small, but less general

# refer to the Editorial page for complexity analysis of these approaches.


import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        h_sz = len(nums) - k + 1

        for n in nums:
            heapq.heappush(h, -n)

            if len(h) > h_sz:
                heapq.heappop(h)
        
        return -h[0]
