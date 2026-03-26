# submission: https://leetcode.com/problems/path-sum-ii/submissions/1959939529/
# runtime: 0 ms (beats 100.00%), memory: 20.18 MB (beats 80.70%)
# 18 min

# TC: (V + E) -> O(n + (n-1)) -> O(n), where n is the number of nodes in the tree
# SC: O(h), where h is the height of the tree (recursion stack); doesn't count the output space


# this problem is a classic tree problem. it could be solved using DFS or BFS. i employed DFS here and implemented as below. note that we also need backtracking technique to keep track of the current path list.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        ans = []

        
        def dfs(node, path, curr_sum):
            assert node is not None

            if node.left is None and node.right is None:    # node is a leaf
                if curr_sum == targetSum:
                    ans.append(path[:])
                return
            
            if node.left is not None:
                path.append(node.left.val)
                dfs(node.left, path, curr_sum + node.left.val)
                path.pop()

            if node.right is not None:
                path.append(node.right.val)
                dfs(node.right, path, curr_sum + node.right.val)
                path.pop()
        

        dfs(root, [root.val], root.val)
        return ans
