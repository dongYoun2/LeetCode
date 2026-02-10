# submission: https://leetcode.com/problems/partition-equal-subset-sum/submissions/1908512084/
# time limit exceeded
# 24 min

# TC: O(2^n), where n is the length of the input list `nums`.
# SC: O(n) (recursion stack; recursion tree height)

# this approach is a brute-force approach; pure dfs/backtracking, without using memoization. 

# the idea and the logic itself of the code below is correct, but it fails due to the time limit exceeded error. to solve this, we can use memoization; we can cache the state, not the chosen list (`cands`). for more details, refer to the README.md.


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, s = len(nums), sum(nums)
        assert n > 0
        if s % 2 == 1:
            return False

        half_s = s // 2

        ans = False
        def dfs(cands, next_pos, curr_sum):
            if curr_sum == half_s:
                nonlocal ans
                ans = True
                return
            
            if curr_sum > half_s:
                return
            
            for i in range(next_pos, n):
                cands.append(nums[i])
                dfs(cands, i + 1, curr_sum + nums[i])
                cands.pop()


        dfs([], 0, 0)
        return ans


# notes while solving:
# 1 5 11 5

# after sort: 1 5 5 11

# 1 4 19 19 19 19 19 100

# 1 2 3 4 5 6 7 8
