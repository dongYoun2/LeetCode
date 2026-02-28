# submission: https://leetcode.com/problems/task-scheduler/submissions/1780787724/
# wrong Solution
# 31 min


# idea was that we can place "all" of the tasks with the highest frequency first, then fill the IDLE slots if needed. i repeated this process until all the tasks are placed while keeping track of the count of tasks.

# however, we can easily notice that this approach doesn't work for the failed test case in the submission link.


from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cntr = Counter(tasks)

        task_freqs = sorted(list(cntr.items()), key=lambda e: e[1], reverse=True)
        sorted_tasks = [t for t, _ in task_freqs]

        intervals = []
        while True:
            curr_cnt = 0
            for task in sorted_tasks:
                if cntr[task] > 0:
                    intervals.append(task)
                    curr_cnt += 1
                    cntr[task] -= 1

            if not any(list(cntr.values())):
                break

            if curr_cnt <= n:
                for _ in range(n - curr_cnt + 1):
                    intervals.append('!')   # '!' is a placeholder indicating IDLE

        return len(intervals)
