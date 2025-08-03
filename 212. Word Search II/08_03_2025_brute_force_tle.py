# submission: https://leetcode.com/problems/word-search-ii/submissions/1722370005/
# Time Limit Exceeded

# Refer to the markdown file for the variable notations.

# TC: O(W * m * n * 4^L * L), last L is for the python slicing in the find function.
# SC: O(m*n + L + L^2) -> O(m*n + L^2). visited + recursion stack + slicing considering the recursion.


# From LeetCode Top Interview 150 - Trie

# This is a brute force solution where you loop over each word and explore all cells in the board, doing a DFS for each cell (see the last for loop part in the code below). Therefore, this is very expensive and will lead to TLE.

# I knew this problem is a Trie problem, but I wanted to try the brute force solution first to see how it works.

# For a correct solution, refer to the markdown file.


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        dys = [-1, 0, 1, 0]
        dxs = [0, 1, 0, -1]

        is_valid = lambda r, c: 0 <= r < m and 0 <= c < n


        def find(r, c, seg):
            if len(seg) == 0:
                return True

            ret = False
            for dy, dx in zip(dys, dxs):
                nxt_r, nxt_c = r + dy, c + dx

                if is_valid(nxt_r, nxt_c) and not visited[nxt_r][nxt_c] and board[nxt_r][nxt_c] == seg[0]:
                    visited[nxt_r][nxt_c] = True

                    ret = ret or find(nxt_r, nxt_c, seg[1:])

                    visited[nxt_r][nxt_c] = False

            return ret


        ans = set()
        for word in words:
            for r in range(m):
                for c in range(n):
                    if board[r][c] == word[0]:
                        visited[r][c] = True
                        if find(r, c, word[1:]):
                            ans.add(word)
                        visited[r][c] = False

        return list(ans)
