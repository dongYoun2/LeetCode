# submission: https://leetcode.com/problems/subsets/submissions/1921216558/
# runtime: 0 ms, memory: 19.67 MB
# 10 min

# TC: O(n*2^n), where n is the length of `nums` (n copy for each of the 2^n subsets)
# SC: O(n) (max recursion stack space)


# solved it using a backtracking approach. though i knew that using python itertools.combinations is the simplest and most efficient way, i first used a backtracking since that's the purpose of this problem. many combinations, permutations, products, etc. problems can be solved with a backtracking approach. this problem can also be solved with BFS.

# two things to note:
# 1. memoization is not needed since the problem doesn't have any overlapping subproblems.
# 2. `nonlocal ans` is not necessary since we are not reassigning the `ans`.

# cf.) BFS submission link: https://leetcode.com/problems/subsets/submissions/1921253714/
# itertools.combinations submission link: https://leetcode.com/problems/subsets/submissions/1921245189/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def dfs(i, curr):
            # nonlocal ans
            if i >= n:
                ans.append(curr[:])
                return
            
            dfs(i+1, curr)
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
                
        dfs(0, [])
        return ans
