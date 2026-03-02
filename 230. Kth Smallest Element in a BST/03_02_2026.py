# submission: https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/1936048973/
# runtime: 3 ms (beats 31.21%), memory: 22.05 MB (beats 89.27%)
# 5 min

# time and space complexity is the same as the "05_02_2025.py" solution. refer to it for details.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        assert root is not None
        cnt = 0
        ans = -1
        
        def inorder_traverse(root):
            nonlocal cnt, ans
            if root is None: return
            inorder_traverse(root.left)
            cnt += 1
            if cnt == k:
                ans = root.val
                return

            inorder_traverse(root.right)
        
        inorder_traverse(root)

        return ans
