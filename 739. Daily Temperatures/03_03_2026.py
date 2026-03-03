# submission: https://leetcode.com/problems/daily-temperatures/submissions/1936798481/
# runtime: 100 ms (beats 50.93%), memory: 28.19 MB (beats 84.54%)
# 10 min

# complexity analysis is the same as the solution in the README.md. refer to it for details.


# i remember this problem cause i was amazed by the idea of using monotonic stack before. so i directly tried to simulate using the stack data structure, and was able to solve it.


from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack:
                prev_i = stack[-1]
                prev_t = temperatures[prev_i]
                if  t > prev_t:
                    ans[prev_i] = i - prev_i
                    stack.pop()
                else:
                    break
            stack.append(i)
        
        return ans


# notes while solving:
# 100K
# TC upper bound: O(n)
# monotonic stack
