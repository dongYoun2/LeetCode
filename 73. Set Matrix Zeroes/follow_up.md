

## Using `set` to Track Rows and Columns

I think this approach has the most clean and readable code. Although the second code uses $O(1)$ space, this code is more readable. Since execution time is a bigger deal than memory usage (and linear space is manageable), faster and more readable code is preferred. Moreover, while this and the second approach have the same time complexity, in practice, this approach executes twice as much faster. I believe this is due to the number of passes in the code.

- [Submission](https://leetcode.com/problems/set-matrix-zeroes/)
- TC: $O(mn)$
- SC: $O(m+n)$

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        zero_row_set, zero_col_set = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row_set.add(i)
                    zero_col_set.add(j)

        for i in range(m):
            for j in range(n):
                if i in zero_row_set or j in zero_col_set:
                    matrix[i][j] = 0

```
<br>


## LeetCode Editorial's Approach 2: O(1) Space, Efficient Solution

- [Submission](https://leetcode.com/problems/set-matrix-zeroes/) (submitted to compare the complexity)
- TC: $O(mn)$
- SC: $O(1)$

```python
class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well
        if is_col:
            for i in range(R):
                matrix[i][0] = 0

```