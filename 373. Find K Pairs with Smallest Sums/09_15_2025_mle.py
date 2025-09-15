# submission: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/submissions/1771997307/
# Memory Limit Exceeded

# 45 min
# TC: O((n1*n2) * log (n1*n2))
# SC: O(n1*n2)


# i spent around 45 minutes on this problem, and the resulting code i implemeted is as below. however, it got a memory limit exceeded error. i believe the logic is correct, but the number of elements that could be stored in the heap is in the worst case n1*n2. this is actually too large considering that the n1 and n2 can be at most 10^5.

# not only the space but also the time complexity is too large. in the worst case, we are iterating through all the combinations of nums1 and nums2, and for each, we are pushng to the heap twice, and popping once, which takes n1*n2*log(n1*n2) time. therefore, i realized i needed to further optimize the code, and eventually came up with the code in `09_15_2025.py` and solved it.



import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        min_n = min(n1, n2)

        pq = []
        ans = []

        for b in range(min_n):
            heapq.heappush(pq, (nums1[b] + nums2[b], (nums1[b], nums2[b])))
            p, t = heapq.heappop(pq)
            ans.append(t)

            if len(ans) >= k:
                break

            for i in range(b + 1, n2):
                priority = nums1[b] + nums2[i]
                tup = (nums1[b], nums2[i])
                heapq.heappush(pq, (priority, tup))

            for j in range(b + 1, n1):
                priority = nums1[j] + nums2[b]
                tup = (nums1[j], nums2[b])
                heapq.heappush(pq, (priority, tup))

            p, t = heapq.heappop(pq)
            ans.append(t)

            if len(ans) >= k:
                break

        while len(ans) < k:
            p, t = heapq.heappop(pq)
            ans.append(t)

        return ans
