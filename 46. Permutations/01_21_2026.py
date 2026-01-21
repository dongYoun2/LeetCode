# submission: https://leetcode.com/problems/permutations/submissions/1892653586/
# runtime: 3 ms, memory: 19.70 MB
# 9 min

# time and space complexity are the same as the **Backtracking** solution described in the README.md


# this problem is a typical backtracking problem

# cf.) using a set `seen` allows to perform membership check in O(1) time, which is more efficient than using a list


from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(curr: List[int], seen: set):
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return

            for n in nums:
                if n not in seen:
                    curr.append(n)
                    seen.add(n)
                    dfs(curr, seen)

                    seen.remove(n)
                    curr.pop()
            
        
        dfs([], set())

        return ans
