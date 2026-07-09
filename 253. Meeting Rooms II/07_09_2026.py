# submission: https://leetcode.com/problems/meeting-rooms-ii/submissions/2062169920/
# runtime: 7 ms (beats 84.20%), memory: 21.29 MB (beats 95.14%)
# 41 min
# algorithm and the complexity analysis is the same as the "03_25_2025.py" solution.


# this is a brute-force solution. refer to the README.md for the heap solution.

# spent too much time, and even solved with a brute-force approach. just like in "10_02_2025.py", i first sorted by the end time. i think i was trying to solve from my memory, and confused with the "452. Minimum Number of Arrows to Burst Balloons" problem (i really need to approach logically). after submitting several wrong submissions (submission 10-13), i was thinking 'wait, do i need to sort by the start time?' just by chance. then, i only changed this sorting logic from the submission 13, and it worked.. i should really not solve problems like this.

# btw, bc of the input length constraints, i assumed i should solve in O(n log n) time. however, i still tried brute-force (linear) search approach since previous attempts (submission 10-12) all failed.


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        charged = [intervals[0]]
        for i in range(1, n):
            swapped = False
            for prev_interval in charged:
                if prev_interval[1] <= intervals[i][0]:
                    prev_interval[1] = intervals[i][1]
                    swapped = True
                    break
            
            if not swapped:
                charged.append(intervals[i])
        
        return len(charged)
