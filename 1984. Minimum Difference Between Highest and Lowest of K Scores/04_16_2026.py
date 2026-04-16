# submission: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/submissions/1980042262/
# runtime: 7 ms (beats 68.67%), memory: 19.33 MB (beats 60.20%)
# 6 min

# TC: O(n log n)
# SC: O(1)


# chose the problem from the "sliding window" category.

# knew this is a sliding window problem. burte force solution would be simply trying all possible combinations of k scores. in this case, the time complexity is O(nCk * k), and when k = n/2, it takes exponential time, which is the worst case.

# from the problem requirement that we have to choose the highest and lowest scores among k scores, we can first think of sorting the array. then, we can use a sliding window with a fixed window size of k to find the minimum difference.


import math

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = math.inf
        for i in range(len(nums)-k+1):
            ans = min(ans, nums[i+k-1] - nums[i])
        
        return ans
