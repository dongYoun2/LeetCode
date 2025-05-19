# submission: https://leetcode.com/problems/permutations/submissions/1638434111/

# 9 min
# runtime: 3 ms, memory: 17.9 MB
# TC: O(n*n!), where n is the length of `nums`.
# SC:
# - O(n): recursion stack
# - O(n): `curr_perm` list
# - O(n^2): `cands` slices. At depth d, we have to hold a n-d size list. Across all d levels from 0 to n-1, we have to hold a total of n + (n-1) + (n-2) + ... + 1 = n*(n+1)/2 = n*(n+1)/2 = O(n^2) in memory.
# --> Altogether, O(n + n + n^2) = O(n*(n+2)) -> O(n^2)

# From LeetCode Top Interview 150 - Backtracking

# The solution below uses a backtracking algorithm to generate all permutations.

# The space complexity can be further reduced to O(n) (only the recursion stack space) by avoiding the use of slicing.

# This can be further optimized by using an index instead of slicing, reducing the space complexity to O(n) since only the recursion stack space is used. For more details, refer to the markdown file.


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs_backtrack(curr_perm, cands):
            if not cands:
                ans.append(curr_perm[:])
                return

            for idx, n in enumerate(cands):
                curr_perm.append(n)
                dfs_backtrack(curr_perm, cands[:idx] + cands[idx+1:])
                curr_perm.pop()


        dfs_backtrack([], nums)

        return ans