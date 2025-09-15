# submission: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/submissions/1772032258/
# runtime: 121 ms, memory: 34.9 MB

# 65 min (including the time spent on `09_15_2025_mle.py`)
# TC: O(k * log k)
# SC: O(k)


# after getting a memory limit exceeded error in `09_15_2025_mle.py`, i realized that i needed to optimize the code. after popping an element (a_i, b_j) from the heap, i noticed that i only need to push the next two elements (a_i+1, b_j) and (a_i, b_j+1) to the heap instead of all (a_{i+k}, b_j) for all 1 <= k < len(nums1) and all (a_i, b_{j+l}) for all 1 <= l < len(nums2). this is because the next two elements are the only ones that can be the next smallest sum. one caveat is that we need to keep track of the elements that we have already pushed to the heap to avoid duplicates. this is done by using a `inserted` set (just like the `visited` set in DFS or BFS algorithms).


import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        min_n = min(n1, n2)

        pq = []
        ans = []
        inserted = set()

        create_heap_elem = lambda i, j: (nums1[i] + nums2[j], (i, j, (nums1[i], nums2[j])))

        elem = create_heap_elem(0, 0)
        heapq.heappush(pq, elem)
        inserted.add((0, 0))

        while len(ans) < k:
            p, (i, j, tup) = heappop(pq)
            ans.append(tup)

            if i + 1 < n1 and (i + 1, j) not in inserted:
                e = create_heap_elem(i + 1, j)
                heapq.heappush(pq, e)
                inserted.add((i + 1, j))

            if j + 1 < n2 and (i, j + 1) not in inserted:
                e = create_heap_elem(i, j + 1)
                heapq.heappush(pq, e)
                inserted.add((i, j + 1))

        return ans
