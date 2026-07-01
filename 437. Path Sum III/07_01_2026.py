# submission: https://leetcode.com/problems/path-sum-iii/submissions/2052314703/
# runtime: 137 ms (beats 30.54%), memory: 47.16 MB (beats 5.05%)
# 19 min
# solved with dfs + path-sum list (all path sums ending at the current node)

# TC: O(n*h), where n is the number of nodes in the tree and h is the height of the tree
# - while traversing the tree, we scan all path sums at each node
# - worst: h = n (skewed tree)
# - average: h = log n (balanced tree)
# SC: O(h)


# first, i thought i could simply use level order traversal with bfs, and count all the path sums equal to the target sum. however, noticing that the path doesn't always have to start at the root or end at a leaf node, i started thinking about using dfs. since the path for this problem can be in the middle of the root-leaf path, i observed that we can leverage prefix sum technique. idk why but i felt the time complexity would be much larger than the problem requirements. so while, looking for other approaches, i simulated that for each node, i can pass down the array of all path sums ending at the current node. considering the problem constraints that n <= 1K, i thought this solution would be acceptable. 

# cf.) though actually, the approach of passing down the prefix sum array also has the exact same time complexity, lol. this approach can be found in the "07_01_2026_prefix_sum_list.py" file.

# cf.) the reason "07_01_2026_prefix_sum_list.py" is almost twice faster and uses less memory in practice compared to this solution although the complexity analysis is the same is because the former solution doesn't recreate a new list, and instead mutate the existing list, whereas this solution recreates a new list (`l_sums`, `r_sums`) at each node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        
        ans = 0

        
        def dfs(node, sums):
            assert node is not None

            nonlocal ans
            for s in sums:
                if s == targetSum:
                    ans += 1

            if node.left is not None:
                l_sums = [s + node.left.val for s in sums]
                l_sums.append(node.left.val)
                dfs(node.left, l_sums)

            if node.right is not None:
                r_sums = [s + node.right.val for s in sums]
                r_sums.append(node.right.val)
                dfs(node.right, r_sums)
        

        dfs(root, [root.val])
            
        return ans
