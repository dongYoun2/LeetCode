# submission: https://leetcode.com/problems/task-scheduler/submissions/1780827504/
# runtime: 101 ms (beats 57.25%), memory: 20.01 MB (beats 86.67%)
# 55 min (including writing the wrong solution; 09_24_2025_wrong.py)


# symbols:
# - T: total task instances (length of tasks)
# - K: number of unique tasks (number of capital letters == 26)
# - n: cooldown period (same `n` in the code below)
# - L: final schedule length; tasks + idles (length of `intervals`)

# TC:
# - build counts + heapify: O(T) + O(K)
# - heap operations across all tasks: each task instance is popped once and (unless it finishes) pushed once  => O(T log K)
# - intervals construction: O(L)
# - therefore: O(T log K + L) -> O(T + L) (since K is bounded by 26)
# - cf.) worst case: when n is large and only few unique tasks, then L = T + (T - 1) * n = O(T*n). thus, TC becomes O(T + T*n) = O(T*n).

# SC: O(K + L) -> O(L) since K is bounded by 26
# - cf.) worst case, where single task type and large n: O(T*n)


# i solved this problem using priority queue. after failing with the code in `09_24_2025_wrong.py`, i noticed that i have to use the priority queue since we have to place (or process) the task with the highest frequency first. this is a typical greedy approach with priority queue data structure. (i was actually amazed that i could recognize the mean heap property on LC bc i have never been able to do that before. i usually knew which algorithm to use in advanc since i solve problems based on the algorithm category.)

# so the code below exactly simulates the taks scheduling process and build the intervals. however, this could be further optimized since we only need the number of intervals (time) (no need to actually build the intervals). for more details, refer to the README.md file.


import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cntr = Counter(tasks)
        task_freqs = list((-freq, task) for task, freq in cntr.items())

        heapq.heapify(task_freqs)

        intervals = []
        while task_freqs:
            tasks_in_cycle_cnt = len(task_freqs)
            next_round_tasks = []
            for _ in range(min(tasks_in_cycle_cnt, n + 1)):
                    minus_freq, task = heapq.heappop(task_freqs)
                    intervals.append(task)

                    if minus_freq + 1 < 0:
                        next_round_tasks.append((minus_freq + 1, task))

            if next_round_tasks and tasks_in_cycle_cnt < n + 1:
                for _ in range(n - tasks_in_cycle_cnt + 1):
                    intervals.append('!')

            for item in next_round_tasks:
                heapq.heappush(task_freqs, item)

        return len(intervals)
