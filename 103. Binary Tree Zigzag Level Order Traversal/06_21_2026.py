# submission: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/2041474024/
# runtime: 0 ms (beats 100.00%), memory: 19.48 MB (beats 48.12%)
# 9 min
# solved using bfs

# refer to the "05_01_2025.py" for a complexity analysis.


# this is a typical bfs problem. it's simply level-order traversal, but we need one flag variable to indicate whether to reverse the order of the nodes at each level.


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        ans = []
        is_reversed = False
        q = deque([root])

        while q:
            nodes = []
            for _ in range(len(q)):
                curr = q.popleft()
                nodes.append(curr.val)

                if curr.left is not None:
                    q.append(curr.left)
                
                if curr.right is not None:
                    q.append(curr.right)
            
            if is_reversed:
                nodes.reverse()
            
            ans.append(nodes)
            is_reversed = not is_reversed

        return ans
        