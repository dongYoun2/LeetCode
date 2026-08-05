# submission: https://leetcode.com/problems/jump-game-ii/submissions/2094625256/
# runtime: 19 ms (21.80%), memory: 20.29 MB (beats 99.99%)
# 20 min (time includes writing "08_04_2026.py" solution)
# solved with a greedy algorithm (but sc is not optimal; refer to the README.md's Greedy Approach section for the optimal greedy implementation)

# TC: O(n), where n is the length of nums
# SC: O(n) (for the `min_arr` array; optimal greedy solution can be done in O(1) space)


# after solving with the forward dp approach (08_04_2026.py) and looking at the runtime graph, i was sure that there is a O(n) time solution. since i suspected the greedy algorithm before, i could easily find the greedy idea.

# the key point is to keep track of the fartest reachable index at each step (`idx_so_far`). because i came from solving with dp approach, i didn't consider whether `min_arr` (`dp` array in a dp solution code) is truly needed. so i simply kept it and store the minimum number of jumps for each and every index, which requires O(n) space. in fact, we can easily solve with O(1) space (for O(1) space greedy solution, refer to the README.md's Greedy Approach section).

# additionaly, though the code below has a nested loop, the `idx_so_far` prevents revisiting already covered indices. therefore, the entire loop runs at most n times.


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        min_arr = [0] * n
        min_arr[0] = 0
        idx_so_far = 0
        for i in range(n-1):
            to_idx = min(i+nums[i], n-1)
            for pos in range(idx_so_far+1, to_idx+1):
                min_arr[pos] = min_arr[i] + 1

            idx_so_far = max(idx_so_far, to_idx)

        return min_arr[-1]
