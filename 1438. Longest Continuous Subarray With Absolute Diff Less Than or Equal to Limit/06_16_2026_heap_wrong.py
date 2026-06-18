# submission: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/submissions/2035652194/
# wrong solution
# 30 min (includes time writing "06_16_2026_sorting_tle.py")


# chose from a neetcode "sliding window" category.

# as mentioned in the "06_16_2026_sorting_tle.py", i tried using the heap data structure. however, this is a wrong solution since we cannot guarantee that the `h[-1]` is the maximum value. in heap, only the minimum value is guaranteed to be the root.

# cf.) lol, idk why assumed `h[-1]` is the maximum value.

# cf.) for the extension of this approach, we can solve this problem in O(n log n) time by:
# 1. using two heaps (min heap and max heap), and
# 2. storing the indices of the elements in the heap as well.


import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        h = [nums[0]]
        l = 0
        ans = 1
        for r in range(1, n):
            heapq.heappush(h, nums[r])

            if h[-1] - h[0] <= limit:
                ans = max(ans, r - l + 1)
            else:
                if nums[l] == h[-1]:
                    h.pop()
                elif nums[l] == h[0]:
                    while heapq.heappop(h) != nums[l+1]:
                        pass

                l += 1
        
        return ans
