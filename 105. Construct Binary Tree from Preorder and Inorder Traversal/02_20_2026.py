# submission: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/1925544077/
# runtime: 39 ms (beats 53.23%), memory: 21.34 MB (beats 53.43%)
# 21 min

# refer to the 04_22_2025_passing_indices.py for the complexity analysis.


# i was tempted to use list slicing since that's more straightforward. however, knowing that slicing has extra overhead, i refrained from using it, and instead directly passed the indices as arguments. (the code below is a little verbose than the "04_22_2025_passing_indices.py", but the main logic is the same.)

# cf.) note that using hash table to store the indices of the inorder traversal at once as a preprocessing step can reduce the time complexity to O(n). for more details, refer to the README.md file.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build_tree(pre_s, pre_e, in_s, in_e):
            if pre_s > pre_e:
                return None

            root_val = preorder[pre_s]
            in_root_idx = inorder.index(root_val)

            l_cnt = in_root_idx - in_s
            r_cnt = in_e - in_root_idx

            l_pre_s = pre_s + 1
            l_pre_e = l_pre_s + l_cnt - 1
            l_in_s = in_s
            l_in_e = l_in_s + l_cnt - 1

            left = build_tree(l_pre_s, l_pre_e, l_in_s, l_in_e)

            r_pre_s = l_pre_e + 1
            r_pre_e = pre_e
            r_in_s = in_root_idx + 1
            r_in_e = in_e

            right = build_tree(r_pre_s, r_pre_e, r_in_s, r_in_e)
            
            root = TreeNode(root_val, left, right)

            return root


        return build_tree(0, len(preorder) - 1, 0, len(inorder) - 1)
