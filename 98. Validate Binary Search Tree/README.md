[Problem](https://leetcode.com/problems/validate-binary-search-tree/)

Among three approaches below, the bounds checking recursion approach is usually regarded as the most concise and straightforward solution, and the complexity is also optimal.

## Bounds Checking Recursion 

- [Submission](https://leetcode.com/problems/validate-binary-search-tree/submissions/1630465505/) (Runtime: 0 ms, Memory: 19.9 MB)
- TC: $O(n)$, where $n$ is the number of nodes in the tree.
- SC: $O(h)$, where $h$ is the height of the tree. (worst case: $h = n$)

The below solution uses a recursive helper function to check if the current node's value is within the valid range defined by its ancestors. The range is updated as we traverse down the tree. The valid range for the left child is defined by the minimum value and the current node's value, while the valid range for the right child is defined by the current node's value and the maximum value. Initial minimum and maximum values can be set to either negative or positive infinity, or the minimum and maximum values that a node can take defined by the problem constraints.

cf.) The main difference between this approach and the [Return Min, Max, and Validity from a Subtree](#return-min-max-and-validity-from-a-subtree) approach is that the former is more like a **top-down** style, where we pass the constriants down, whereas the latter is **bottom-up** (bubbling up) style, where the parent node checks whether children fit BST rules.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper_is_valid(root_, min_val, max_val):
            if root_ is None: return True
            if not (min_val < root_.val < max_val): return False

            return helper_is_valid(root_.left, min_val, root_.val) and helper_is_valid(root_.right, root_.val, max_val)

        # return helper_is_valid(root, -float('inf'), float('inf'))
        return helper_is_valid(root, -(2**31 + 1), 2**31)
```

## Inorder Traversal Approach 

Refer to the [05_10_2025.py](./05_10_2025.py) for detailed explanation.


## Return Min, Max, and Validity from a Subtree

Refer to the [01_13_2025.py](./01_13_2025.py) for detailed explanation.
