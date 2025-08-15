# submission: https://leetcode.com/problems/jump-game/submissions/1732317544/
# runtime: 21 ms, memory: 18.6 MB

# 16 min
# TC: O(n), where n is the length of nums
# SC: O(1)

# cf.) although the solution below uses two loops, it is still O(n) because the inner loop will not run more than n times in total across all iterations of the outer loop.


# From LeetCode Top Interview 150 - Array / String

# not until i submit the code below, did i realize that the solution is a greedy algorithm and that the problem could also be solved using dynamic programming.

# there are two edge cases that i missed before i successfully solved the problem:
# 1. `nums` with length 1 should always return True, since you are already at the last index. but the actual logic doesn't handle this case so i added the early return.
# 2. `nums` where the first element can directly jump beyond the last index (e.g. [2, 0], [8, 3, 1, 1, 4]). because of this case, `if max_curr_idx >= len(nums) - 1:` statement is necessary right after the while loop starts. (Before, i wrote this condition at the end of the while loop, which fails to this case.)

# this solution can be improved while keeping the same greedy approach. it can be improved by keeping only one loop. for more details, refer to the markdown file.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        curr_idx = 0
        max_curr_idx = curr_idx + nums[curr_idx]

        while curr_idx != max_curr_idx:
            if max_curr_idx >= len(nums) - 1:
                return True

            for i in range(curr_idx + 1, max_curr_idx + 1):
                next_max = i + nums[i]

                if next_max >= max_curr_idx:
                    max_curr_idx = next_max
                    curr_idx = i

        return False
