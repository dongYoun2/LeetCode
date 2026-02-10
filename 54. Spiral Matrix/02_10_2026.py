# submission: https://leetcode.com/problems/spiral-matrix/submissions/1915046106/
# runtime: 0 ms (Beats 100.00%), memory: 19.45 MB (Beats 22.82%)
# 43 min


# took too long than i expected. previously, i solved this problem in recursive approach (03_28_2025.py) in 22 minutes. it took twice longer this time and the code itself is quite messy. debugging took long. feels like instead of logically thinking and solving, i was kind of trying to make the code pass the failed test cases. also, i attempted during the ccm course, and maybe i couldn't focus well (good excuse lol). hope to solve it better next time. 

# cf.) compare the difference between this code and the codes in the README.md.


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        r_start, c_start = 0, -1
        r_end, c_end = m-1, n-1

        cnt = 0
        ans = []

        while cnt < m * n:
            c_start += 1
            for j in range(c_start, c_end+1):
                ans.append(matrix[r_start][j])
                cnt += 1
            if cnt == m * n: break

            r_start += 1
            for i in range(r_start, r_end+1):
                ans.append(matrix[i][c_end])
                cnt += 1
            if cnt == m * n: break

            c_end -= 1
            for j in range(c_end, c_start-1, -1):
                ans.append(matrix[r_end][j])
                cnt += 1
            if cnt == m * n: break

            r_end -= 1
            for i in range(r_end, r_start-1, -1):
                ans.append(matrix[i][c_start])
                cnt += 1
        
        return ans
