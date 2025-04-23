# problem: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# submission: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/1615822854/

# 17 min
# runtime: 5 ms, memory: 19.54 MB
# TC: O(n), where n is the number of nodes in the tree
# SC: O(n + n) -> O(n) (for the `inorder_cache` and the recursion stack)

# From LeetCode Top Interview 150 - Binary Tree General

# This is simply a variation of the previous problem, "105. Construct Binary Tree from Preorder and Inorder Traversal." I solved and reviewed it yesterday. So, for this problem, I could directly apply the similar logic with the two optimization techniques that I commented on yesterday.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        assert len(inorder) == len(postorder)

        def helper_build_tree(in_s, in_e, post_s, post_e):
            if in_e - in_s < 0: return None

            root_val = postorder[post_e]

            pos = inorder_cache[root_val]

            left_len = pos - in_s
            right_len = in_e - pos

            left = helper_build_tree(in_s, in_s + left_len - 1, post_s, post_s + left_len - 1)
            right = helper_build_tree(pos + 1, (pos + 1) + right_len - 1, post_s + left_len, (post_s + left_len) + right_len - 1)

            return TreeNode(root_val, left, right)

        inorder_cache = {v: i for i, v in enumerate(inorder)}
        return helper_build_tree(0, len(inorder) - 1, 0, len(postorder) - 1)
