# submission: https://leetcode.com/problems/decode-ways/submissions/2058067755/
# Time Limit Exceeded (the logic is correct)
# 17 min
# used DFS

# TC: O(2^n), becuase for each index, we have two choices: either take one digit or two digits.
# SC: O(n) (the recursive stack)


# i recognized this problem as a dfs problem, though i was a little suspicious of the time complexity. i implemented the recursive dfs solution, and got TLE. it's quite straightforward to notice that the pure brute-force dfs would take exponential time.

# so, i assumed it's not a dfs problem, and while keeping thinking of other approaches, i felt like it's a dp problem (at 29 min). however, since i limited myself to 30 minutes, i didn't implement it, and tried to look up the solution, but just in case, i checked the topic tag, and was correct that it's a dp problem.

# thus, i implemented the dp solution ("07_06_2026_dp.py"), and was able to solve the problem.


# cf.) though i completely gave up this dfs solution, and kept thinking of other approaches, this solution can be turned into a top-down dp solution by simply adding an optimization (memoization) technique. this optimized solution can be found here: https://leetcode.com/problems/decode-ways/submissions/2059707814/—runtime: 0 ms (beats 100.00%), memory: 19.41 MB (beats 22.53%). this submission code is a little different from the README.md's top-down dp code since the latter defines the recurrent relation as "dp[i] = number of ways to decode s[:i]" (so, `dp[i] = dp[i-1] + dp[i-2]`), whereas the former defines as "dp[i] = number of ways to decode s[i:]" (so, `dp[i] = dp[i+1] + dp[i+2]`). In short, the difference is whether the substring is taken as the prefix or the suffix.


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        ans = 0


        def dfs(idx):
            nonlocal ans

            if idx >= n:
                ans += 1
                return
            
            if s[idx] == '0':
                return

            dfs(idx+1)
            
            if idx+1 < n and (s[idx] == '1' or (s[idx] == '2' and '0' <= s[idx+1] <= '6')):
                dfs(idx+2)


        dfs(0)
        return ans
