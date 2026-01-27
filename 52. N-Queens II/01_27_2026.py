# submission: https://leetcode.com/problems/n-queens-ii/submissions/1899093673/
# runtime: 21 ms (beats 19.43%), memory: 19.42 MB (beats 20.84%)
# 34 min

# TC: O(n! * (n + n^2)) -> O(n! * n^2), where n is the size of the board
#   - O(n!): number of search nodes (placements tried): order of the number of partial permutations of columns
#   - O(n): (per node) `find_invalid_cells_below` loops over rows below
#   - O(n^2): (per node) set `invalid_cells` can grow up to n^2 elements
# SC: O(n * n^2) -> O(n^3)
#   - O(n): recursion depth
#   - O(n^2): (per node) set `invalid_cells` can grow up to n^2 elements


# From LeetCode Top Interview 150 - Backtracking

# N-queens is a well-know problem that can be solved with backtracking, but this is actually my first time solving it. 

# The code below can be further optimized by using additional diagonal and anti-diagonal tracking arrays to avoid the set operation which reduces the time and space complexity. For more details, refer to the README.md.


class Solution:
    def totalNQueens(self, n: int) -> int:
        def find_invalid_cells_below(r, c):
            ret = set()
            j_left = c - 1
            j_right = c + 1
            for i in range(r+1, n):
                ret.add((i, c))
                if j_left >= 0:
                    ret.add((i, j_left))
                if j_right < n:
                    ret.add((i, j_right))

                j_left -= 1
                j_right += 1
            
            return ret
        
        
        def find_queen_pos(r, c, invalid_cells):
            if r == n - 1:
                nonlocal ans
                ans += 1
                return
            
            for j in range(n):
                if (r+1, j) not in invalid_cells:
                    invalid_cells_cp = invalid_cells.copy()
                    new_invalid = find_invalid_cells_below(r+1, j)
                    invalid_cells_cp.update(new_invalid)
                    find_queen_pos(r+1, j, invalid_cells_cp)


        ans = 0
        for j in range(n):
            find_queen_pos(0, j, find_invalid_cells_below(0, j))
        
        return ans
