# submission: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/submissions/1617625995/

# 54 min (spent around 45 min on "04_25_2025_wrong.py" and 9 min on this one)
# TC: O(n^2) (skewed tree: worst-case), where n is the number of nodes in the tree (balanced tree: O(n log n))
# - the reason the time complexity is not O(n) is because we need to find the tail of the flattened left subtree through `while` loop, which takes O(n) time. however, this can be avoided by using a tail pointer, which takes O(1) time, leading the entire time complexity to be O(n).
# SC: O(n) (recursion stack)

# From LeetCode Top Interview 150 - Binary Tree General

# At first, I didn't catch the main idea of the solution. I tried to copy the tree, then reconstruct the flattened tree on the original tree while traversing the copied tree in preorder. When copying the tree, I tried Python's deepcopy` but it seemed not to be working for a tree data structure (actually it works. I just tested again and realized it works.. I don't know why I thought it didn't work..). So, I tried to manually copy the tree using preorder traversal. Although I manually copied the tree, I should be able to solve it. However, it took too long to debug the code ("04_25_2025_wrong.py").

# I switched a gear toward starting from scratch. Then, I realized that this problem could be solved by a recursive approach. The main idea is to flatten the left and right subtrees of the root node, then attach the flattened left subtree to the right of the root node and attach the flattened right subtree to the right of the last node of the flattened left subtree. It's always good to keep in mind that the tree-related problems can be solved by a recursive approach due to the recursive nature of the tree data structure.

# cf.) While writing the above comment, I retried using the approach that I attempted on "04_25_2025_wrong.py", but with a Python `deepcopy`. Now, I could solve it in 7 min ("04_25_2025_deepcopy.py"). At that moment, I guess my brain wasn't working well since I attempted this problem right after I woke up, haha.

# cf.) For the optimal solution and the solution for the follow up question, refer to the markdown file.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper_flatten(root_):
            if root_ is None: return None

            flattened_left = helper_flatten(root_.left)
            flattened_right = helper_flatten(root_.right)
            root_.left = None

            if flattened_left is not None:
                find = flattened_left   # find tail of the flattened_left
                while find.right:
                    find = find.right

                find.right = root_.right
                root_.right = flattened_left

            return root_

        helper_flatten(root)
