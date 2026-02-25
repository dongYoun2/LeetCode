# submission: https://leetcode.com/problems/word-search/submissions/1931183083/
# this solution directly attempts to solve the follow-up question
# runtime: 744 ms (beats 93.30%), memory: 19.72 MB (beats 7.34%)
# 32 min

# refer to the README.md for the complexity analysis. the code below doesn't use extra space to track the visited cells. instead, it marks the visited cells with '#' character in place, so the space complexity is O(w) (for recursion stack), where 'w' is the length of the word.


# i approached with dfs backtracking as soon as i saw the problem. noticing there's a follow-up question, i tried to think some pruning techniques that could be applied to this problem. i submitted the first solution with only the first pruning technique (https://leetcode.com/problems/word-search/submissions/1931181180/). noticing that the runtime takes long, i applied the second pruning, which checks if the word is achievable with the given board based on the character count. there's also a one last pruning technique: "search-ordering heuristic". for more details, refer to the README.md.


from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # prune 1
        if len(word) > m*n: return False

        b_cntr = Counter(cell for row in board for cell in row)
        w_cntr = Counter(word)
        
        # prune 2
        if w_cntr - b_cntr:
            return False

        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]

        is_valid = lambda r, c: 0 <= r < m and 0 <= c < n

        def dfs(y, x, w_idx):
            if board[y][x] != word[w_idx]:
                return False

            if w_idx + 1 >= len(word):
                return True

            backup = board[y][x]
            board[y][x] = '#'
            
            for dy, dx in zip(dys, dxs):
                yn, xn = y + dy, x + dx

                if is_valid(yn, xn) and dfs(yn, xn, w_idx + 1):
                    return True
                    
            
            board[y][x] = backup
            return False

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
