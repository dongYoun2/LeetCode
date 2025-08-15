# submission: https://leetcode.com/problems/jump-game-ii/submissions/1735954249/
# runtime: 964 ms, memory: 19.37 MB

# 26 min
# TC: O(V+E), where V (# of verticies) is equal to n, the length of nums, and E (# of edges) is <= n^2 in the worst case.
# SC: O(n), for the queue and `visited` set


# From LeetCode Top Interview 150 - Array / String

# as i recently solved the "55. Jump Game" problem, i felt like this problem can also be solved using greedy algorithm. however, it was a little tricky to think of and suddenly my thoughts went to a BFS solution. It's simply a level-order traversal and the minimum number of jumps is equal to the number of levels traversed. Since we may visit the same index multiple times, we need to keep track of visited indices to optimize the search.

# i realized i really need to practice greedy algorithms more. it always feels hard to find it's a greedy problem as well as to implement it correctly.


from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
       q = deque([0])
       visited = {0}
       ans = 0

       while q:
        q_size = len(q)
        for _ in range(q_size):
            curr = q.popleft()

            if curr >= len(nums) - 1:
                return ans

            for nxt in range(curr + 1, curr + nums[curr] + 1):
                if nxt not in visited:
                    q.append(nxt)
                    visited.add(nxt)

        ans += 1
