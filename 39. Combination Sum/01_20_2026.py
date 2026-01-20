# submission: https://leetcode.com/problems/combination-sum/submissions/1891453981/
# runtime: 4 ms, memory: 19.8 MB
# 27 min


# refer to the README.md for the complexity analysis.

# took longer than expected because i took too much time debugging. it turned out that i forgot to "copy" the current combination when appending to the answer list.


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()
        def dfs(pos, curr, curr_target):
            if curr_target == target:
                ans.append(curr.copy())
                return
            
            for i in range(pos, n):
                c = candidates[i]
                if curr_target + c > target:
                    break
                
                curr.append(c)
                dfs(i, curr, curr_target + c)
                curr.pop()
        

        dfs(0, [], 0)

        return ans
