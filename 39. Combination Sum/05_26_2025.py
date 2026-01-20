# submission: https://leetcode.com/problems/combination-sum/submissions/1645531539/
# runtime: 412 ms, memory: 18 MB
# 11 min


# - With the extra symbols below in addtion to the symbols used in the README.md:
# - r: number of unique combinations returned (size of the `ans`)

# TC: O(N^d + r * d \log d) -> O(N^d)
# - O(N^d): Total number of calls in the DFS tree; at each node, we loop over all N candidates, and we can go as deep as d.
# - O(r * d \log d): We have total r "solution" leaf nodes, and for each of them, we sort the current combination of candidates, which takes O(d \log d) time.

# reasoning for simpliyfing the time complexity:
# 1. since r <= O(N^d), O(N^d + r * d \log d) <= O(N^d + N^d * d \log d) == O(N^d * (1 + d \log d)) == O(N^d * d \log d)
# 2. since a polynomial term (d \log d) is dominated by the exponential term (N^d), O(N^d * d \log d) == O(N^d)

# SC: O(2*d) -> O(d) (O(d) for the recursion stack and current combination storage respectively)


# From LeetCode Top Interview 150 - Backtracking

# After implementing the solution with a backtracking algorithm, the problem was that the same combination would be counted multiple times—e.g., [2,2,3] and [2,3,2] would be counted as different combinations. I used sorting, a tuple, and a set to prevent this issue. However, this approach is not optimal, as it sorts the current combination at each leaf node, which can be costly. Instead of sorting solution candidates every time, I realized that the duplicates can also be avoided by passing the current cursor index to the recursive function, which is a more efficient way. This approach is in "05_26_2025_backtracking_with_index.py".



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(curr, remain):
            if remain == 0:
                ans.add(tuple(sorted(curr[:])))
                return

            if remain < 0:
                return

            for candidate in candidates:
                curr.append(candidate)
                dfs(curr, remain - candidate)
                curr.pop()


        ans = set()
        dfs([], target)

        return list(ans)