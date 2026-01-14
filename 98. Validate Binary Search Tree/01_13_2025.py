# submission: https://leetcode.com/problems/validate-binary-search-tree/submissions/1884315588/
# runtime: 4 ms, memory: 21.08 MB

# 35 min
# TC: O(n), where n is the number of nodes in the tree
# SC: O(h), where h is the height of the tree. (worst case: h = n)


# the main idea is to return min, max, and validity of a subtree and bubble it up to the parent node to check if the entire tree is a valid BST.

# it took longer than expected since i need to consider how to handle the case where left child, right child, or both doesn't exist. since we are checking the validity of the subtree, returned min and max values are not necessarily correct (it's only correct if the subtree is a valid BST).

# cf.) the code is a bit verbose. better solution would be "Bounds Checking Recursion" approach. for more details, refer to the README.md.


from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        assert root is not None


        def is_valid(node: TreeNode) -> Tuple[int, int, bool]:  # subtree's min, max, validness
            assert node is not None
            
            l_min = l_max = node.val
            curr_valid = True
            if node.left is not None:
                l_min, l_max, l_valid = is_valid(node.left)
                curr_valid = curr_valid and l_valid and l_max < node.val
            
            r_min = r_max = node.val
            if node.right is not None:
                r_min, r_max, r_valid = is_valid(node.right)
                curr_valid = curr_valid and r_valid and node.val < r_min

            return l_min, r_max, curr_valid
            

        return is_valid(root)[2]
