# submission: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/submissions/2097260460/
# runtime: 83 ms (beats 63.91%), memory: 39.81 MB (beats 34.24%)
# 28 min
# solved using heap

# refer to the README.md for a complexity analysis


# i really needed to logically and mathematically think about which tuple is always smaller than the other tuple, etc. assuming current tuple is (i, j), once i found out that i can simply push (i+1, j) and (i, j+1) into the heap, i directly implemented that way.

# however, one caveat is that then there may be a duplicated tuples inserted, which is shown in this wrong submission: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/submissions/2097257819/. thus, we need to keep track of the already pushed tuples (using `seen` set below) to avoid duplicated tuples.

# cf.) below implementation is essentially the same as the README.md's solution.


import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        ans  = []
        heapq.heappush(h, (nums1[0]+nums2[0], 0, 0))
        seen = {(0, 0),}
        while len(ans) < k:
            _, i, j = heapq.heappop(h)
            ans.append([nums1[i], nums2[j]])

            if i+1 < len(nums1) and (i+1, j) not in seen:
                heapq.heappush(h, (nums1[i+1]+nums2[j], i+1, j))
                seen.add((i+1, j))
            if j+1 < len(nums2) and (i, j+1) not in seen:
                heapq.heappush(h, (nums1[i]+nums2[j+1], i, j+1))
                seen.add((i, j+1))

        return ans
