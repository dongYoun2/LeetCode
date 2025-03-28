# problem: https://leetcode.com/problems/valid-sudoku/
# submission: https://leetcode.com/problems/valid-sudoku/submissions/1588742974/

# 29 min
# TC: O(n^2) (Although Sudoku is 9x9, TC is expressed with n for generality, where n is the length of the board. In this situation, each row, column, and sub-box contains the digits 1 to n without duplicates. Also, the size of the sub-box is always (square root of n) x (square root of n), so only the square number can be 'n'.)
# SC: O(n^2) (python set)

# It was a pretty interesting question. I knew how to transpose a 2D matrix with pure Python. However, it was a bit confusing to map each 3x3 sub-box index to the original index. I could come up with the general index conversion formula by thinking carefully about one example. Each sub-box is represented via (y, x), and each element in the sub-box is represented via (i, j). In fact, this reminds me of the CUDA parallel programming during the MPC course. 1) Mapping the sub-box index to the original index is exactly the same as converting the 2d matrix index to the 1d array index, and 2) mapping the sub-box index to the converted index is exactly the same as computing the global index using the block index and thread index.

# Below code needs 5 passes (each for transposing matrix, converting sub-boxes to rows, checking rows, columns, and 3x3 sub-boxes) to check the validity of the Sudoku. However, this can be optimized to 1 pass (But the time complexity is still O(n^2)). There are n rows, n columns, and n sub-boxes. For each element in the board, we can check the validity of the row, column, and sub-box at the same time. One thing to notice is how to compute the index for the i-th sub-box. It can be computed by (r//3)*3 + c//3, where r and c are the row and column index of the element in the board. For mor details, refer the LeetCode Editorial.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_rows(board_):
            for row in board_:
                s = set()
                for e in row:
                    if e != ".":
                        if e in s:
                            return False
                        s.add(e)

            return True


        board_T = [list(col) for col in zip(*board)]

        converted_board = [[-1] * 9 for _ in range(9)]
        for y in range(3):
            for x in range(3):
                for i in range(3):
                    for j in range(3):
                        to_y, to_x = 3*y+x, 3*i+j
                        from_y, from_x = 3*y+i, 3*x+j
                        converted_board[to_y][to_x] = board[from_y][from_x]

        return check_rows(board) and check_rows(board_T) and check_rows(converted_board)

# notes while solving this problem:
# tile: (0, 1), inner: (2, 1)
# (y,x) (i, j) --> converted: (3*y+x, 3*i+j) (1, 7)
# (y,x) (i, j) --> original: (3*y+i, 3*x+j) (2, 4)
