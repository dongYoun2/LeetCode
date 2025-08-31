# submission: https://leetcode.com/problems/jump-game-ii/submissions/1754975826/
# runtime: 4 ms, memory: 18.71 MB

# 6 min
# TC: O(n), where n is the length of nums
# SC: O(1)


# From LeetCode Top Interview 150 - Array / String

# after solving using DP (08_31_2025.py), i tried with a greedy appraoch. it's pretty straightforward as i remember this problem. the main idea is to keep track of maximum reachable index (max offset) while iterating through the `nums` array (variable `nxt_max_reach_idx` works the same as the `max_offset` in a greedy solution in README.md). Once the current index reaches the `max_reach_idx`, the minimum number of jumps (the answer) as well as the `max_reach_idx` have to be updated.


class Solution:
    def jump(self, nums: List[int]) -> int:
        min_cnt = 0
        max_reach_idx = 0
        nxt_max_reach_idx = 0

        for i in range(len(nums)):
            if i > max_reach_idx:
                min_cnt += 1
                max_reach_idx = nxt_max_reach_idx

            nxt_max_reach_idx = max(nxt_max_reach_idx, i + nums[i])

        return min_cnt
