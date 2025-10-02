# submission: https://leetcode.com/problems/meeting-rooms-ii/submissions/1789227664/
# runtime: 3 ms, memory: 19.78 MB

# 51 min
# TC: O(n log n + 2 * n log n) -> O(n log n), where n is the length of the `intervals`.
# - sorting takes O(n log n) time.
# - in the worst case, maximum number of heappop operations we can do for the loop is n. moreover, for each interval, we are doing heappush operation. so, total heappop/heappush related time complexity is (2 * n log n) -> O(n log n).
# - therefore, O(n log n) counting both sorting and heappop/heappush TC.
# SC: O(n), for the priority queue.


# it took more time than i expected to solve this problem. at first, i sorted based on the end time, and i really don't know from what logic i sorted this way. i guess i simply thought that what i need is the earliest meeting room that is available without checking the start time. so failing on several submissions, i realized that i needed to sort based on the start time, and then use a priority queue to pop all the meeting rooms that already ended at the current meeting's (or interval's) start time.

# however, the code below can be slightly improved. for more details, refer to the markdown file.

# cf.) i remembered that this problem is solved by greedy approach, so at first attempt, i didn't even think logically and simply checked whether the previous meeting's end time is less than or equal to the current meeting's start time.. (wrong submission: https://leetcode.com/problems/meeting-rooms-ii/submissions/1789191904/)


import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort() # sort by the start time
        pq = [(intervals[0][1], intervals[0])]
        ans = 1

        for i in range(1, n):
            while pq and pq[0][0] <= intervals[i][0]:
                heapq.heappop(pq)

            heapq.heappush(pq, (intervals[i][1], intervals[i]))
            ans = max(ans, len(pq))

        return ans
