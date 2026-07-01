# submission: https://leetcode.com/problems/path-sum-iii/submissions/2052322933/
# runtime: 83 ms (beats 35.71%), memory: 19.82 MB (beats 78.87%)
# 28 min (time including the "07_01_2026.py" solution)
# solved with dfs + prefix sum list

# complexity analysis is the same as the "07_01_2026.py" solution.


# this solution can be considered as the improved version of the "07_01_2026.py" solution. there are two main improvements:
# 1. pass down the tue prefix sum array as a parameter of the dfs recursive function.
# 2. mutate the existing prefix sum array (doesn't recreate a new list) so that it reduces the overhead of consuming extra memory.

# cf.) however, we can still further optimize this solution by using dfs (w/ backtracking) + prefix sum + hash map. this cuts down the TC to O(n) from O(n*h). i was flabbergasted by this clever solution. the key idea is to simply compute the previous prefix sum we need in constant time by computing (current prefix sum) - (target sum), which allows us to leverage the hash table data structure.

# refer to this submission for the optimized solution: https://leetcode.com/problems/path-sum-iii/submissions/2052377018/—Runtime: 5 ms (beats 68.41%), Memory: 20.82 MB (beats 17.76%)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        
        ans = 0


        def dfs(node, ances_pre_sums):
            nonlocal ans
            curr_sum = ances_pre_sums[-1] + node.val
            for s in ances_pre_sums:
                if curr_sum - s == targetSum:
                    ans += 1
            
            ances_pre_sums.append(curr_sum)

            if node.left is not None:
                dfs(node.left, ances_pre_sums)
                ances_pre_sums.pop()

            if node.right is not None:
                dfs(node.right, ances_pre_sums)
                ances_pre_sums.pop()


        dfs(root, [0])
            
        return ans
