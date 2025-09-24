# submission: https://leetcode.com/problems/daily-temperatures/submissions/1781336113/
# time limit exceeded

# this s a brute force solution, where the time complexity is O(n^2).


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        candidates = {0}    # indices candidates
        ans = [0] * n

        for i in range(1, n):
            for j in list(candidates):
                if temperatures[j] < temperatures[i]:
                    ans[j] = i - j
                    candidates.remove(j)

            candidates.add(i)

        return ans
