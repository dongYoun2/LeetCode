# problem: https://leetcode.com/problems/binary-search-tree-iterator/
# submission: https://leetcode.com/problems/binary-search-tree-iterator/submissions/1619550834/

# 25 min
# TC:
#     - O(h) for __init__(), where h is the height of the tree
#     - O(1) (amortized) for next()
#     - O(1) for hasNext()
# SC:
#     - O(n) (structural space) for stack, wher n is the number of nodes in the tree
#     - O(h) (auxiliary space) for __init(), next(), and hasNext()

# if tree is balaned, h is O(log n), whereas if tree is skewed, h is O(n)

# From LeetCode Top Interview 150 - Binary Tree General

# In the beginning, I tried to use only pointers to traverse the tree. However, I realized that since I could not go back up to the parent node, I needed to use a stack. Then, I could quite easily implement the algorithm.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        assert root is not None
        self.stack = deque()

        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left


    def next(self) -> int:
        node = self.stack.pop()

        curr = node.right

        while curr:
            self.stack.append(curr)
            curr = curr.left

        return node.val


    def hasNext(self) -> bool:
        return bool(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()