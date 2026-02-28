# submission: https://leetcode.com/problems/task-scheduler/submissions/1934022187/
# runtime: 121 ms (beats 53.38%), memory: 20.93 MB (beats 35.34%)
# 18 min

# refer to the README.md for time and space complexities since they are the same as the "Greedy with Priority Queue" solution there.


# i faintly remembered that this problem is a greedy problem so i was trying to figure out how to approach with a greedy algorithm. while simulating the task scheduling process with pen and paper, using priority queue popped up at some point. basically, i maintained the counter to keep track of the frequency of each task, and put each task in a heap with "(next_available_time, task)". so, this allows to always pick the task that becomes available the earliest. after running a task, i decreased its remaining count, and pushed the task back with new available time = current_time + n + 1. therefore, the code simulates the timeline directly.

# i was a little surprised that i solved it in 18 min without looking at any hints (there were 3 hints).

# cf.) a notable difference between a typical greedy solution for this problem is that this solution doesn't always choose the most frequent task first. instead, it picks earliest available task. it's still a greedy solution, but on a different priority.


from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cntr = Counter(tasks)
        pq = [(0, task) for task in cntr]   # same priorities in the beginning
        for task in cntr:
            cntr[task] -= 1
        
        ans = 0
        while pq:
            idx, task = heapq.heappop(pq)
            if idx > ans:
                ans = idx
            
            if cntr[task] > 0:
                cntr[task] -= 1
                heapq.heappush(pq, (idx + n + 1, task))

            ans += 1

        return ans
