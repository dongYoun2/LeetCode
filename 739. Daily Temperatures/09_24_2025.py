# submission: https://leetcode.com/problems/daily-temperatures/submissions/1781356057/
# runtime: 2445 ms, memory: 26.42 MB

# 43 min (includes writing time limit exceeded code; 09_24_2025_tle.py)
# TC: O(N * K), where N is the length of temperatures and K is the number of possible temperatures (30 <= temperature <= 100)
# SC: O(K)


# i used hash map to store the nearest future index for each temperature, and iterated through temperatures backward. this approach is affordable because the number of possible temperatures is limited to only 71 (30 <= temperature <= 100). howveer, if this scale increases, we need to use a more efficient approach.

# the more efficient method, which actually is the intention of this problem, is to use a (monotonic) stack. for more details,s refer to the README.md file.


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [float('inf')] * n
        cache = {t: -1 for t in range(30, 101)} # temp -> nearest future index

        for i in range(n - 1, -1, -1):
            curr_temp = temperatures[i]
            for temp in range(curr_temp + 1, 101):
                if cache[temp] >= 0:
                    ans[i] = min(ans[i], cache[temp] - i)

            cache[curr_temp] = i

        for i in range(n):
            if ans[i] == float('inf'):
                ans[i] = 0

        return ans


# notes while solving:
# 100 99 98 97 96 95

# 73 74 75 71 69 72 76 73

# 30 30 30 30 30 30 30