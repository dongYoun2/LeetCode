# submission: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/submissions/1797375767/
# runtime: 49 ms, memory: 19.03 MB

# 7 min
# TC: O(n), where n is the number of nodes in the tree
# SC: O(n) (more precisely, O(w), where w is the maximum width of the tree)


# the problem is quite straightforward. we can solve it by level-order traversl while keeping the previous node pointer.

# cf.) follow-up question was tough. for more details, refer to the markdown file.


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None

        q = deque([root])

        while q:
            q_size = len(q)
            prev = None
            for _ in range(q_size):
                curr = q.popleft()
                if prev:
                    prev.next = curr
                prev = curr

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return root
