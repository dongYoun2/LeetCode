

## Using `set` to Track Rows and Columns

I think this approach has the most clean and readable code. Although the second code uses $O(1)$ space, this code is more readable. Since execution time is a bigger deal than memory usage (and linear space is manageable), faster and more readable code is preferred. Moreover, while this and the second approach have the same time complexity, in practice, this approach executes twice as much faster. I believe this is due to the number of passes in the code.

Moreover, this code solves the problem in two passes, unlike `09_17_2025_follow_up_1.py` which solves the problem in three passes.

- [Submission](https://leetcode.com/problems/set-matrix-zeroes/submissions/1595825601/)
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


## Solution for the Follow-up Question 2: O(1) Space, Efficient Solution

The logic is as follows:
1. First pass: remember which rows/cols must be zero using the first row/col as marker storage.
2. Second pass: zero all non-first-row/col cells based on those markers.
3. Finally: handle whether the first row/col themselves should be zeroed, tracked by two booleans.

- [Submission](https://leetcode.com/problems/set-matrix-zeroes/submissions/1774978805/)
- TC: $O(mn)$
- SC: $O(1)$

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        # Check if first row or first column need to be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero cells based on markers (skip first row/col for now)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

```

Notes: When I tried to solve the follow-up question 2, I thought of converting zeros that are encountered while changing rows/cols values to zeros as negative ones, and later on, converting negative ones back to zeros. However, this approach doesn't work since the value range is all possible values for 4 byte integer, which is from -2^31 to 2^31-1. (If values are restricted to positive integers, this approach works.)
