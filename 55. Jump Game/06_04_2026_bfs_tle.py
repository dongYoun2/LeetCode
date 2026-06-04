# submission: https://leetcode.com/problems/jump-game/submissions/2022682972/
# time limit exceeded
# 12 min
# bfs solution

# - TC: O(V + E) -> O(n) + O(n^2) -> O(n^2)
#   - V: number of vertices = n
#   - E: number of edges <= n * (n - 1) / 2
# - SC: O(n) (for the queue and the visited set)


# this is the first solution i came up with on 06/04/2026. i analyzed the time complexity before, and noticed it's O(n^2). in the problem constraints, "n" a be at most 10K. i always consider mapping 500 to O(n^3), 2K to O(n^2), and 100K to O(n log n). so, though i assumed the optimal solution would have TC less than O(n log n), but i still tried the BFS first. as expected, i got TLE.


from collections import deque

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = {0,}
        q = deque([0])
        while q:
            curr = q.popleft()
            if curr == n - 1:
                return True

            for i in range(curr+1, curr+nums[curr]+1):
                if i not in visited:
                    q.append(i)
                    visited.add(i)

        return False
