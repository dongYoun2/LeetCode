
### Iterative Approach

The iterative approach uses nested loops and tracks the boundaries of the matrix with 4 variables (i.e. r_start, r_end, c_start, c_end). This is more efficient in terms of total space complexity, which reduces to O(1).

- [Submission](https://leetcode.com/problems/spiral-matrix/submissions/)
- TC: O(m*n)
- SC: O(1)

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


