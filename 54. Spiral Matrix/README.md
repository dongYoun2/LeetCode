
### Iterative Approach

Unlike the recursive solution `03_28_2025.py`, iterative approach is more efficient in terms of total space complexity, which reduces to $O(1)$.

cf.) All codes below set up boundaries using 4 variables. Another way is to track the visited cells. We can mark visited cells on the original matrix in place (no additional space needed), or use a separate visited matrix or set (requires additional space).


### Using Direction (`direc`) Variable

The code below is an iterative version of the recursive solution `03_28_2025.py`. It uses nested loops and tracks the boundaries of the matrix with 4 variables (i.e. `r_start`, `r_end`, `c_start`, `c_end`). Also, `direc` variable helps us to track the direction of the traversal.

[Submission](https://leetcode.com/problems/spiral-matrix/submissions/1589290947/)—Runtime: 0 ms (Beats 100.00%), Memory: 17.80 MB (Beats 63.44%)

- TC: $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the matrix.
- SC: $O(1)$

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r_start = c_start = 0
        r_end = len(matrix) - 1
        c_end = len(matrix[0]) - 1

        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
        direc = RIGHT

        ans = []
        while r_start <= r_end and c_start <= c_end:
            if direc == RIGHT:
                for k in range(c_start, c_end + 1):
                    ans.append(matrix[r_start][k])
                r_start += 1
            elif direc == DOWN:
                for k in range(r_start, r_end + 1):
                    ans.append(matrix[k][c_end])
                c_end -= 1
            elif direc == LEFT:
                for k in range(c_end, c_start - 1, -1):
                    ans.append(matrix[r_end][k])
                r_end -= 1
            else:   # direc == UP
                for k in range(r_end, r_start - 1, -1):
                    ans.append(matrix[k][c_start])
                c_start += 1

            direc = (direc + 1) % 4

        return ans
```


### No Direction Variable

We can also solve this problem without using the direction variable. In this case, we have to be cautious that no duplicated rows or columns are traversed multiple times. This is prevented by the two `if` guards in the main `while` loop in the below codes.


[Submission](https://leetcode.com/problems/spiral-matrix/submissions/1915075834/)—Runtime: 0 ms (Beats 100.00%), Memory: 19.48 MB (Beats 23.37%)
- TC: $O(m \cdot n)$
- SC: $O(1)$

The code right below is the same as the Editorial section's Approach 1.

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top = left = 0
        bottom, right = m-1, n-1
        ans = []
    
        # we can also use "while top <= bottom and left <= right" for the termination condition
        while len(ans) < m * n:
            for j in range(left, right+1):
                ans.append(matrix[top][j])

            for i in range(top+1, bottom+1):
                ans.append(matrix[i][right])
            
            # to ensure the row is different from the one we traversed from left to right
            # easy to understand the need of this guard when considering the single row matrix
            if top != bottom:
                for j in range(right-1, left-1, -1):
                    ans.append(matrix[bottom][j])

            # to ensure the column is different from the one we traversed from top to bottom
            # easy to understand the need of this guard when considering the single column matrix
            if left != right:
                for i in range(bottom-1, top, -1):
                    ans.append(matrix[i][left])
            
            top += 1
            right -= 1
            bottom -= 1
            left += 1
        
        return ans

```

Instead of updating the 4 boundary variables at the end of the main `while` loop, we can update the relevant boundary at the end of each traversal (the `for` loops). In this case, the `if` guards conditions become slightly different. Also, this is cleaner since `range(...)` arguments are consistent across the traversals (`for` loops).


[Submission](https://leetcode.com/problems/spiral-matrix/submissions/1915105227/)—Runtime: 0 ms (Beats 100.00%), Memory: 19.48 MB (Beats 23.37%)

Time and space complexity are the same as the previous code.

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top = left = 0
        bottom, right = m-1, n-1
        ans = []

        # while len(ans) < m * n:
        while top <= bottom and left <= right:
            for j in range(left, right+1):
                ans.append(matrix[top][j])
            top += 1

            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                for j in range(right, left-1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1
        
        return ans

```
