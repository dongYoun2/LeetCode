# https://leetcode.com/problems/meeting-rooms-ii/

# 16 min
# TC: O(nlog n + n^2) -> O(n^2)
# SC: O(n)

# This is a greedy algorithm, making the local optimal choice.
# 1. Always trying to assign an existing meeting room.
# 2. If no meeting rooms are availabe, add a new room.

# I scanned through all existing rooms to check if any of them were freed. As soon as I found one, I assigned that room (due to the greedy property, which exact room to assign doesn't matter. At first, I wasn't sure about this.). However, this takes O(n) time complexity for each interval in a worst-case scenario, leading to O(n^2) for all intervals.

# How can we do better? When finding a freed room, we can directly find a room that has the earliest end time instead of checking all existing rooms' end times. This can be done by using min heap (priority queue), which makes the overall time complexity as O(nlog n + n) -> O(nlog n). Check the markdown file for the heap solution.


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda elem: elem[0])

        rooms = []
        for interval in intervals:
            inserted = False
            for i in range(len(rooms)):
                if rooms[i][1] <= interval[0]:
                    rooms[i] = interval
                    inserted = True
                    break

            if not inserted:
                rooms.append(interval)

        return len(rooms)


# notes while solving the problem

# 0                30
#   5  10
#          15  20


# [0, 15] [2, 4] [2, 6]

# 0        15
#   2 4
#   2    6