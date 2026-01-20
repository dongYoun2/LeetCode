# submission: https://leetcode.com/problems/combination-sum/submissions/1815344415/
# runtime: 3 ms, memory: 17.77 MB

# 17 min
# refer to the README.md for the complexity analysis.


# pretty straightforward to implement. two points to note:
# 1. since the `curr_comb` list is passed by reference, we need to deepcopy it when appending to the answer list, as well as popping it when backtracking.
# 2. prune when the current candidate is greater than the remaining sum. (to do this, we needed to sort the candidates list in advance.)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def comb_sum(curr_comb: List[int], pos: int, remain: int):
            if remain == 0:
                ans.append(curr_comb[:])
                return

            for i in range(pos, len(candidates)):
                if candidates[i] > remain:
                    return

                curr_comb.append(candidates[i])
                comb_sum(curr_comb, i, remain - candidates[i])
                curr_comb.pop()


        comb_sum([], 0, target)
        return ans
