import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(heap, (-(n1+n2), (n1, n2)))

                if len(heap) > k:
                    heapq.heappop(heap)

        ans = []
        for _ in range(k):
            _, (n1, n2) = heapq.heappop(heap)
            ans.append([n1, n2])


        return ans[::-1]
