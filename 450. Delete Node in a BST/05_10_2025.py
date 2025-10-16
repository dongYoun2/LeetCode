# submission: https://leetcode.com/problems/delete-node-in-a-bst/submissions/1630385150/
# runtime: 4 ms, memory: 21.5 MB

# 37 min
# TC: O(h), where h is the height of the tree
# SC: O(h) (for recursion stack)

# I tried this problem on the extension of the follow-up question of the "230. Kth Smallest Element in a BST's follow-up question." I remembered that I have learned BST insertion and deletion in the Data Structure course during my undergrad.

# However, it was a bit tricky to implement, so it took quite a long time as I forgot the details of the deletion process. At first, I coded up without considering the case where the root node is the one to be deleted, which raised the runtime error (https://leetcode.com/problems/delete-node-in-a-bst/submissions/1630369031/). I fixed it by adding a dummy node to the root node, which is a common technique. After fixing that, I also realized that I didn't consider the case where the node to delete doesn't have the right child (https://leetcode.com/problems/delete-node-in-a-bst/submissions/1630379805/). I fixed it by falling back to the left child.

# After fixing all the above issues, I was able to solve the problem correctly, but the code readability is very poor. Refer to the Editorial section for a more readable and typical BST node deletion solution. Editorial approach divides the logic into three cases—whether deleting a node is a 1) leaf node, 2) node with right child, or 3) node with only left child. Also, it separately implements methods to find the successor and predecessor nodes of the deleting node in the BST inorder traversal. (BST inorder traversal is always sorted in ascending order.)

# cf.) Note that my solution deletes a node in a BST by subtree-relinking, which physically splices out the node object itself, whereas the Editorial solution deletes a node by value-copy technique, where the logical deletion happens by copying the value up to the parent node until the leaf node of the deleting node's subtree is reached. This is why my code needs to keep track of the parent node of the deleting node, whereas the Editorial solution doesn't need to.

# cf.) after solving this problem again on "10_16_2025.py", i was able to solve it with subtree-relinking approach, without passing the parent node as an argument. moreover, "10_16_2025.py" is more efficient code than the Editorial's solution though it doesn't use the value-copy technique. for more details, refer to the "10_16_2025.py".


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None: return None

        def helper_delete(parent, child):
            if child is None: return

            if key == child.val:
                if parent.left == child:
                    parent.left = child.right if child.right else child.left
                else:   # parent.right == child
                    parent.right = child.right if child.right else child.left


                if child.right is not None:
                    node_to_append_left = child.left

                    find = child.right
                    if find.left is not None:
                        while find.left is not None:
                            find = find.left

                    find.left = node_to_append_left

            elif key < child.val:
                helper_delete(child, child.left)
            else:   # key > child.val
                helper_delete(child, child.right)

        dummy = TreeNode(0, None, root)
        helper_delete(dummy, root)

        return dummy.right
