# submission: https://leetcode.com/problems/merge-intervals/submissions/1894753488/
# runtime: 12 ms, memory: 23.13 MB
# 7 min

# time and space complexity is the same as in the 04_08_2025.py solution.


# straightforward solution.


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda e: e[0])

        s, e = intervals[0]
        ans = [[s, e]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            
            if s <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], e)
            else:
                ans.append([s, e])
        
        return ans
