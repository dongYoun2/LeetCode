# submission: https://leetcode.com/problems/delete-node-in-a-bst/submissions/1803405434/
# runtime: 0 ms, memory: 21.5 MB

# 21 min
# TC: O(h), where h is the height of the tree
# SC: O(h) (recursion stack)


# this is a second time solving this problem. unlike "05_10_2025.py", i didn't need to pass the parent node as an argument to the recursive function. rather, i propagated the deletion result up to the parent node by returning the proper result node.

# cf.) it's interesting to compare this solution with the Editorial's solution. this solution is based on the subtree-relinking approach, whereas the Editorial's solution is based on the textbook "“copy successor/predecessor value, then delete it” pattern" pattern, which performs an extra recursive deletion after copying the value.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_and_delete(node) -> Optional[TreeNode]:
            if not node: return None

            if key == node.val:
                if not node.left or not node.right:
                    return node.left or node.right

                # two children: attach right subtree under the max of left subtree (BST)
                curr = node.left
                while curr.right:
                    curr = curr.right
                curr.right = node.right
                return node.left

            if key < node.val:
                node.left = find_and_delete(node.left)
            else:
                node.right = find_and_delete(node.right)
            return node


        return find_and_delete(root)
