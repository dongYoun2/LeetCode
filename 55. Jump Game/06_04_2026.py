# submission: https://leetcode.com/problems/jump-game/submissions/2022686967/
# runtime: 19 ms (beats 63.83%), memory: 20.24 MB (beats 65.26%)
# 20 min (time including the "06_04_2026_bfs_tle.py")
# solved with a greedy approach

# TC: O(n), where n is the length of nums
# SC: O(1)


# attempted without knowing which algorithm category this problem belongs to. at first, as mentined in the "06_04_2026_bfs_tle.py", i tried a BFS solution. then, i tried to simulate the process assuming the DP approach. meanwhile, i somehow realized that i can simply keep one `max_reach_idx` variable and iterate through the array once, which is a greedy solution and takes O(n) time.

# this code's logic is the same as the "Iterating from the beginning" solution in the "greedy_approach.md" file.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach_idx = 0

        for i in range(n):
            if max_reach_idx >= n - 1:
                return True
            
            if max_reach_idx < i:
                return False

            max_reach_idx = max(max_reach_idx, i + nums[i])

        # will never reach here
