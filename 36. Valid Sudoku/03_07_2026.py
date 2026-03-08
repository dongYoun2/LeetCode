# submission: https://leetcode.com/problems/valid-sudoku/submissions/1941179853/
# runtime: 5 ms (beats 39.08%), memory: 19.36 MB (beats 72.55%)
# 40 min

# TC: O(n^2), where n is the length of the board
# SC: O(n^2) (due to the `block_bard`)
# - by avoiding using `block_board` and directly checking the blocks, we can reduce the space complexity to O(n)
# cf.) with the fixed length of the board (9*9), both time and space complexity are O(1)


# took longer than expected. got stuck while checking the sub-boxes validity. just like in 03_27_2025.py, again, this reminds me of the MCP course where we computed the global index from the block index and the thread index, and flattened the 2D index into a 1D index.

# cf.) note the difference between the 03_27_2025.py and this solution. the former used a 2D array to store the converted board, while this solution used a dictionary to store the blocks.


from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        assert len(board) == 9

        for row in board:
            row_n = [e for e in row if e.isnumeric()]
            if len(row_n) != len(set(row_n)):
                return False
        
        for col in zip(*board):
            col_n = [e for e in col if e.isnumeric()]
            if len(col_n) != len(set(col_n)):
                return False
        
        block_board = defaultdict(list)
        for i in range(9):
            for j in range(9):
                block_i, block_j = i // 3, j // 3
                block_board[(block_i, block_j)].append(board[i][j])
        
        for block in block_board.values():
            block_n = [e for e in block if e.isnumeric()]
            if len(block_n) != len(set(block_n)):
                return False

        return True