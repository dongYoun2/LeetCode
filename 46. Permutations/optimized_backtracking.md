[Problem](https://leetcode.com/problems/permutations/description/)

## Backtracking

Unlike `05_19_2025_backtracking.py`, this code doesn't use slicing. This is because we can simply check if the number is already in the current permutation with `if n not in curr_perm:`. Therefore, we don't need to pass candidate numbers, which are numbers not yet included in the current permutation, to the `dfs_backtrack()` function.

- [Submission](https://leetcode.com/problems/permutations/submissions/1638470472/) (Runtime: 0 ms, Memory: 18 MB)
- TC: $O(n*n!)$, where n is the length of `nums`.
- SC: $O(n)$ (for the recursion stack space).
<br>

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs_backtrack(curr_perm):
            if len(curr_perm) == len(nums):
                ans.append(curr_perm[:])
                return

            for n in nums:
                if n not in curr_perm:
                    curr_perm.append(n)
                    dfs_backtrack(curr_perm)
                    curr_perm.pop()


        dfs_backtrack([])

        return ans

```