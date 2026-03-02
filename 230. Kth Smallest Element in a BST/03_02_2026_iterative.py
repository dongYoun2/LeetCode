# submission: https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/1936055136/
# runtime: 0 ms (beats 100%), memory: 22.23 MB (beats 52.95%)
# 9 min

# time and space complexity is the same as the "05_02_2025.py" solution. refer to it for details.


# after solving in a recursive manner ("03_02_2026.py"), i also solved in an iterative manner using a stack. however, the code below is verbose and we actually don't need `visited` set to implement this approach. for a clean code, refer to the Editorial's "Approach 2: Iterative Inorder Traversal" section.


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        assert root is not None
        stack = deque([root])
        cnt = 0
        visited = set()

        while stack:
            while stack[-1].left is not None and stack[-1].left.val not in visited:
                stack.append(stack[-1].left)

            curr = stack.pop()
            visited.add(curr.val)
            cnt += 1
            if cnt == k:
                return curr.val

            if curr.right is not None:
                stack.append(curr.right)
