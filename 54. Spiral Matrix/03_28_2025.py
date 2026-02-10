# submission: https://leetcode.com/problems/spiral-matrix/submissions/1589288396/

# 22 min
# TC: O(m*n), where m is the number of rows and n is the number of columns in the matrix.
# SC: O(m*n + m*n) -> O(m*n) (Recursive function and visited matrix both requires O(m*n) space complexity, respectively. We can reduce the SC for visited matrix to O(1) by mutating the input matrix, but I believe it is not a good practice.)

# This problem felt like a simulation problem. I had to think when I would want to change the direction of the traversal.

# I used recursive function to implement the spiral order traversal. However, each function call makes at most one furher recursive call, which forms a linear recursive stack, visiting exactly m*n elements. Thus, the time complexity and the space complexity is both O(m*n). However, as the recursion forms a linear stack, we can use iterative approach to implement the same algorithm. For more details, refer to the README.md.

# cf.) I used "if not is_valid(y_n, x_n) or is_visited[y_n][x_n]:" for termination condition in the recursive function. However, this could be replaced with "if len(ans) == m * n:", which is not redundant and more straightforward.


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []

        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        is_valid = lambda y, x: 0 <= y < m and 0 <= x < n
        is_visited = [[False] * n for _ in range(m)]


        def spiral(y, x, direc):
            ans.append(matrix[y][x])
            is_visited[y][x] = True

            dy, dx = directions[direc]
            y_n, x_n = y + dy, x + dx

            if not is_valid(y_n, x_n) or is_visited[y_n][x_n]:
                direc = (direc+1)%4
                dy, dx = directions[direc]
                y_n, x_n = y + dy, x + dx

            if not is_valid(y_n, x_n) or is_visited[y_n][x_n]:
                return

            spiral(y_n, x_n, direc)


        spiral(0, 0, RIGHT)

        return ans


# notes while solving:
# 1 2
# 3 4

# right -> down -> left -> up
