[Problem](https://leetcode.com/problems/subtree-of-another-tree/description/)


## Using DFS


The code below is the refactored version of the `09_29_2025.py` solution, and the logic is the same as the Editorial's Approach 1.

- [Submission](https://leetcode.com/problems/subtree-of-another-tree/submissions/1786587093/) (Runtime: 42 ms, Memory: 18.01 MB)
- TC: $O(m * n)$, where $m$ and $n$ are the number of nodes in the two trees.
- SC: $O(h_1 + h_2)$, where $h_1$ and $h_2$ are the heights of the two trees.
  - balanced case: $h_1 = log(m)$, $h_2 = log(n)$
  - skewed case (worst case): $h_1 = m$, $h_2 = n$


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(r1, r2) -> bool:
            if not r1 or not r2:
                return r1 == r2

            return r1.val == r2.val and is_same(r1.left, r2.left) and is_same(r1.right, r2.right)


        def dfs(node) -> bool:
            if not node:
                return False

            if is_same(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)


        return dfs(root)

```


## String Matching (TC Optimized)

the key is to convert trees into strings and check if the `subRoot` string is a substring of the `root` string.

We have learned during the Data Structures course that two trees are the same if and only if any of two trees' pre-order, in-order, or post-order traversals are the same.

So I converted `subRoot` and `root`'s pre-order and in-order traversls into strings, and checked if `subRoot` string of each traversal is a substring of corresponding `root` string. However, this solution doesn't work here because **different shapes/values can collide as substrings**.

**There are two things to be aware of**:
1. Null nodes should also be included in the string representation. In words, we need a marker for null nodes (`$` is used in the code below).
  - If we don't count null nodes, `root = [4, 1, 2]` and `subRoot = [2]` case will be the counter-example.
2. Separator is needed to distinguish different nodes (or values) since we are converting integers into strings (`^` is used in the code below).


cf.) This solution is the same as the Editorial's Approach 2.


- [Submission](https://leetcode.com/problems/subtree-of-another-tree/submissions/1786598273/) (Runtime: 10 ms, Memory: 18.17 MB)
- TC: $O(m + n)$, where $m$ and $n$ are the number of nodes in the two trees.
- SC: $O(h_1 + h_2)$ (same as the `using DFS` solution)


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        convert = lambda r: '^' + str(r.val) + convert(r.left) + convert(r.right) if r else '$'

        return convert(subRoot) in convert(root)

```


Below is the incorrect code that doesn't count the above two points ([Submission](https://leetcode.com/problems/subtree-of-another-tree/submissions/1786612564/)):

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        pre_main_s = self.preorder(root)
        pre_sub_s = self.preorder(subRoot)

        in_main_s = self.inorder(root)
        in_sub_s = self.inorder(subRoot)

        return pre_sub_s in pre_main_s and in_sub_s in in_main_s

    def preorder(self, root: Optional[TreeNode]) -> str:
        s = ''
        if not root: return s

        s += str(root.val)
        s += self.preorder(root.left)
        s += self.preorder(root.right)

        return s

    def inorder(self, root: Optional[TreeNode]) -> str:
        s = ''
        if not root: return s

        s += self.inorder(root.left)
        s += str(root.val)
        s += self.inorder(root.right)

        return s

```
