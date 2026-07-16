# submission: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/2069952680/
# runtime: 43 ms (beats 88.16%), memory: 19.85 MB (beats 48.78%)
# 64 min
# solved with Multiple dfs w/ Ancestor Path + Opposite Subtree Search

# TC: O(nh + n) -> O(nh), where n is the number of nodes in the tree and h is the height of the tree
# - O(nh): `find_target(...)` since `path` is copied for every recursive call, which can take O(h) time
# - O(n): `search_nodes(...)`
# SC: O(h^2 + h) -> O(h^2)


# finding k distance nodes downward from a target node is not hard in a tree data structure. however, finding nodes upward was challenging. my thought process was as follows:
# 1. find the target node while keep tracking the ancester path of the target node for later use
# 2. find the k distance nodes downward from the target node
# 3. for each ancester node, 1) check if the ancester node itself is at k distance, otherwise 2) check the opposite subtree of the ancester node to find corresponding nodes

# took quite long to implement. i tried not to copy the ancestor path as i knew it would take more time and space, but somehow i was stuck there and debugging took much longer than expected. but still, i couldn't debug properly so eventuallyjust copied the ancestor path, though the TC/SC are not optimal. improved implementation using append()/pop() reduces the TC and SC to O(n) and O(h) respectively. the code can be found here (also searching in the opposite subtree part is under the `else` block to make it more coherent with the above logic): https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/2070281940/—Runtime: 63 ms (beats 6.02%), Memory: 19.79 MB (beats 58.51%)

# cf.) in the beginning, i considered linking a parent node for each node, but i didn't implement this approach, as modifying the existing tree is not a good practice (this is exactly the same as the Editorial section's Approach 1: Implementing Parent Pointers. instead of modifying the tree, we can simply use a hash table to record parent nodes, which is explained in the README.md's "Parent Map + BFS"). moreover, i thought that if the problem was on a graph data structure instead of a tree, where the edge is undirected, it would be much easier to solve since we can simply find the target node, then perform bfs on it (this approach is shown in the README.md's "Graph Construction + BFS"). however, idk why but, my thoughts didn't reach the point of constructing a graph version of a given tree. i think i unconsciously thought and was obsessed with the idea that this problem could be solved by directly performing operations on a tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def find_target(node, path):
            nonlocal ascendents
            assert node is not None

            if node.val == target.val:
                ascendents = path + [(node, 'x')]
                return 

            if node.left is not None:
                find_target(node.left, path + [(node, 'l')])
            
            if node.right is not None:
                find_target(node.right, path + [(node, 'r')])


        def search_nodes(node, curr_h, target_h):
            nonlocal ans

            if node is None:
                return

            if curr_h == target_h:
                ans.append(node.val)
                return
            
            search_nodes(node.left, curr_h + 1, target_h)
            search_nodes(node.right, curr_h + 1, target_h)
        

        ascendents = None
        find_target(root, [])
        assert len(ascendents) > 0

        find, _ = ascendents[-1]
        h_find = len(ascendents) - 1

        ans = []
        search_nodes(find, 0, k)    # from target

        # from ascendents
        for h, (asc, direc) in enumerate(ascendents[:-1]):
            assert asc
            h_diff = k - (h_find - h)

            # check the ascendent itself
            if h_diff == 0:
                ans.append(asc.val)

            # check the other child's subtree of the ascendent
            node = asc.right if direc == 'l' else asc.left
            search_nodes(node, 0, h_diff - 1)
        
        return ans
