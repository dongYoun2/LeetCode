[Problem](https://leetcode.com/problems/jump-game-ii/)

This problem is similar to [55. Jump Game](../55.%20Jump%20Game/greedy_approach.md).


## Greedy Approach

Greedy appraoch is the most efficient way to solve this problem. Both time and space complexity is better than the DP approach. The idea is to keep track of the maximum reachable index at each step and the number of jumps made so far. When the current index reaches the end of the current jump range (`end`), we update the `end`and increment the jump count (`jump_cnt`).


- [Submission](https://leetcode.com/problems/jump-game-ii/submissions/1215353378/)
- Runtime: 103 ms, Memory: 17.54 MB
- TC: $O(n)$, where $n$ is the length of `nums`.
- SC: $O(1)$

<br>

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_offset = 0
        end = 0
        jump_cnt = 0

        for curr in range(len(nums) - 1):
            max_offset = max(max_offset, curr + nums[curr])
            if curr == end:
                end = max_offset
                jump_cnt += 1

        return jump_cnt

```


## Dynamic Programming


### Iterating Backward

Although the time complexity of DP forward and backward is the same, iterating backward is more intuitive as well as faster in practice (see the runtime difference below). This is because:
1. Backward DP allows us to directly compute the minimum jumps needed for each index. In words, we do one write to `dp[i]`, whereas in forward DP, we may write to `dp[j]` multiple times.
2. Backward DP can take advantage of C-optimized techniques like slicing in `min()` operation.


The code here is the optimized version of the `08_15_2025.py` solution. It reflects the improvements discussed in the comments of that file.

- [Submission](https://leetcode.com/problems/jump-game-ii/submissions/1736017736/)
- Runtime: 329 ms, Memory: 18.3 MB
- TC: $O(n^2)$
- SC: $O(n)$

<br>

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [100000] * n   # 100000: maximum possible value

        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] != 0:
                dp[i] = min(dp[i+1:i+nums[i]+1]) + 1

        return dp[0]

```


## Iterating Forward

- [Submission](https://leetcode.com/problems/jump-game-ii/submissions/1735975784/)
- Runtime: 3179 ms, Memory: 18.42 MB
- TC: $O(n^2)$
- SC: $O(n)$

<br>

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        inf = 100_000
        dp = [inf] * len(nums)
        dp[0] = 0

        for i in range(len(nums) - 1):
            max_offset = min(nums[i], len(nums) - 1 - i)
            for j in range(i + 1, i + max_offset + 1):
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[len(nums) - 1]

```


## BFS (with `visited` set)

Refer to the `08_15_2025_bfs.py` solution.
