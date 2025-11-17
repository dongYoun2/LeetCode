# submission: https://leetcode.com/problems/k-closest-points-to-origin/submissions/1832483690/
# runtime: 65 ms, memory: 22.24 MB

# 11 min
# TC: O(n log k), where n is the number of points, and k is the number of closest points to return
# SC: O(k) (heap size of k)


# below is the solution using the heap data structure. i solved this problem using heap once i saw heap (priority queue) in topics tag.

# even using the heap data structure, it's esay to think to first push all elements in the heap, then pop the k elements we need. however, this would be inefficient as the time complexity would be O(n log n + k log n) -> O((n + k) log n). better approach is to simply maintain a heap with a size up to k. specifically, we can push the elements to the heap, and if the size of the heap exceeds k, we can pop the element with the largest distance (furthest from the origin), which allows to keep the heap size of k. Once we iterate through all the points, the final heap contains the k closest points to the origin.

# cf.) we can also use the python's built-in `heapq.nsmallest` function, which has the same time complexity O(n log k). the complete code is only one line "return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)".


import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max-heap maintaining k elements
        heap = []
        for point in points:
            x, y = point
            key = x ** 2 + y ** 2
            heapq.heappush(heap, (-key, point))
            if len(heap) > k:
                _ = heapq.heappop(heap)

        return [p for _, p in heap]
