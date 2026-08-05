[Problem](https://leetcode.com/problems/jump-game-ii/)

This problem is similar to [55. Jump Game](../55.%20Jump%20Game/greedy_approach.md).


## Greedy Approach

Greedy appraoch is the most efficient way to solve this problem. Both time and space complexity is better than the DP approach. The idea is to keep track of the maximum reachable index at each step and the number of jumps made so far. When the current index reaches the end of the current jump range (`end`), we update the `end`and increment the jump count (`jump_cnt`).


[Submission](https://leetcode.com/problems/jump-game-ii/submissions/2094669723/)—Runtime: 4 ms (beats 70.21%), Memory: 19.97 MB (beats 92.78%)


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
1. Each `dp[i]` is computed exactly once, whereas forward DP may update the same `dp[j]` multiple times from different indices.
2. Backward DP can take advantage of C-optimized techniques like slicing in `min()` operation.

The code here is the optimized version of the `08_15_2025.py` solution. It reflects the improvements discussed in the comments of that file.

[Submission](https://leetcode.com/problems/jump-game-ii/submissions/1736017736/)—Runtime: 329 ms (beats 19.23%), Memory: 18.34 MB (beats 100.00%)

- TC: $O(n  \cdot k)$, where $n$ is the length of `nums` and $k$ is the largest possible value of `nums[i]` (i.e., the maximum jump length), which is at most 1000.
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


### Iterating Forward

[Submission](https://leetcode.com/problems/jump-game-ii/submissions/1735975784/)—Runtime: 3179 ms (beats 7.49%), Memory: 18.42 MB (beats 100.00%)


Complexity analysis is the same as the backward iteration, but this approach is slower in practice due to the reasons mentioned above.

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

Refer to the [08_15_2025_bfs.py](./08_15_2025_bfs.py) solution.
