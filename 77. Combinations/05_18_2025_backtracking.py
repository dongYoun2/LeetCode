# submission: https://leetcode.com/problems/combinations/submissions/1637023421/
# runtime: 140 ms, memory: 59.67 MB

# 12 min
# n, k is defines as: Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# TC: O(2^n). This is the worst case where k == n. General case would be O(\Sigma_{i=0}^{k} \binom{n}{i}).
# SC: O(k). This is for the recursion stack, and the output space doesn't count.

# From LeetCode Top Interview 150 - Backtracking

# There were two caveats while solving this problem:
# 1. We cannot simply do `ans.append(comb)` in the termination condition of the recursive function since it would create a reference to the same list object. So, we need to create a copy. Another way to prevent this is instead of doing `comb.append(m)` and `comb.pop()`, we can directly pass the `comb + [m]` to the next recursive call, but this would create a new list object every time. (Still doesn't hurt performance that much)
# 2. We need the early return when the length of the current combination is equal to k. (I knew I had to do it, but forgot at first. kk)

# The code below can be further optimized since partial combinations that can never be reached at size k still exist. This becomes significant when k becomes as large as n. Therefore, finding a maximum start number for the current partial combination further prunes the search space. Fully optimized code can be found in the markdown file.


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs_backtrack(last_num, comb):
            if len(comb) == k:
                ans.append(comb[:])
                return

            for m in range(last_num + 1, n + 1):
                comb.append(m)
                dfs_backtrack(m, comb)
                comb.pop()  # backtrack


        ans = []
        dfs_backtrack(0, [])

        return ans
