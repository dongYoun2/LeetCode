# submission: https://leetcode.com/problems/binary-tree-right-side-view/submissions/1922234380/
# runtime: 0 ms (beats 100%), memory: 19.35 MB (beats 52.41%)
# 5 min

# refer to the 04_29_2025.py for the complexity analysis.


# very straightforward BFS problem.

# instead of checking the last index in the for loop, we can directly append the last node's value to the answer list before the for loop; e.g. ans.append(q[-1].val)


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        ans = []
        q = deque([root])

        while q:
            q_sz = len(q)
            for i in range(len(q)):
                curr = q.popleft()
                if i == q_sz - 1:
                    ans.append(curr.val)
                
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
            
        return ans