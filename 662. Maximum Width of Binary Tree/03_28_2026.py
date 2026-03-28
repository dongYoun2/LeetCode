# submission: https://leetcode.com/problems/maximum-width-of-binary-tree/submissions/
# runtime: 7 ms (beats 19.12%), memory: 20.21 MB (beats 43.37%)
# 14 min

# TC: O(V + E) -> O(N + (N-1)) -> O(N), where N is the number of nodes in the tree.
# SC: O(V) -> O(N)


# i noticed max width could be computed by finding the maximum width of each level. so i came up using bfs to traverse the tree level by level and compute the width of each level. first, i thought of generating a fake node and push it to queue for a null node to fill the gaps between true nodes, but it felt like a waste of memory. while thinking of how to make it better, i realized that we can use the tree node index. left child index is 2 * parent index, and right child index is 2 * parent index + 1. the root node has an index of 1. then the width of each level is computed by "the rightmost node index" - "the leftmost node index" + 1. the implementation is straightforward.

# in practice, for a minute improvement, we can store a relative index (relative to the leftmost node index for each level) instead of the absolute index to prevent integer overflow for the cases where the tree grows very large (deep and wide).

# cf.) we can also use dfs to solve this problem though it's a little more complicated. for details, refer to this submission: https://leetcode.com/problems/maximum-width-of-binary-tree/submissions/1961785722/.


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        assert root is not None

        ans = 1
        q = deque([(root, 1)])
        while q:
            ans = max(ans, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                node, idx = q.popleft()

                if node.left is not None:
                    q.append((node.left, idx * 2))
                if node.right is not None:
                    q.append((node.right, idx * 2 + 1))
        
        return ans
