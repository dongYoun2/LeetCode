# problem: https://leetcode.com/problems/kth-largest-element-in-an-array/
# submission: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1590380972/

# 2 min
# TC: O(n + k log n) (Building heap and popping k times. Worst-case time complexity is O(n log n).)
# SC: O(n)

# The question asks to be solved using something other than sorting. I knew that the quickselect algorithm could solve this problem since it is well known to be one of the most efficient algorithms for finding the K-th largest or smallest element in the array. Also, I knew that I could use heap since I'm currently solving questions based on the algorithm type. Lastly, the LeetCode Editorial introduces 'counting sort' as a solution as well.

# While maintaining the heap data structure, the below code can be further optimized for the time complexity to be O(n log k) by using a min-heap of size k. This is more efficient, especially when k is small relative to n. For more details and the code itself, refer to the LeetCode Editorial.


import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        m_nums = [-n for n in nums]
        heapq.heapify(m_nums)

        for _ in range(k):
            n = heapq.heappop(m_nums)

        return -n
