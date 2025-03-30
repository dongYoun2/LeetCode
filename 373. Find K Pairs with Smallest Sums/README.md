## Heap Solution

- [Problem](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)
- Time complexity: $O(k log(k))$ (looping over k pairs, two heap push operations for each iteration)
- Space complexity: $O(k)$ (heap size of k)

```python
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        cnt = 0
        heap = []

        heapq.heappush(heap, (nums1[0] + nums2[0], (0, 0)))
        visited = {(0, 0)}
        ans = []

        while cnt < k:
            _, (i, j) = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], (i+1, j)))
                visited.add((i+1, j))

            if j + 1 < m and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], (i, j+1)))
                visited.add((i, j+1))

            cnt += 1

        return ans

# simulation:
# pop: (0 0)
# push: (0 1), (1 0)   h = [(0 1), (1 0)] (in any order for simplicity)

# pop: (0 1)
# push: (0 2), (1 1)   h = [(1 0), (0 2), (1 1)]

# pop: (0 2)
# push: (0 3), (1 2)   h = [(1 0), (1 1), (0 3), (1 2)]

# pop: (1 0)
# push: (1 1), (2 0)   h = [(1 1), (0 3), (1 2), (2 0)] ((1 1) has been pushed before, so it should not be pushed again)

```