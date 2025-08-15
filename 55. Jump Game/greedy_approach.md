[Problem](https://leetcode.com/problems/jump-game/)

## Greedy Approach

### Iterating from the end

This problem is actually more natural and straightforward to solve by iterating in the reverse order. (DP approach can also iterate both from the beginning and the end, but it is more intuitive to iterate through backwards. Refer to the Editorial section for more details on the DP solutions.)

- [Submission](https://leetcode.com/problems/jump-game/submissions/1735528698/)
- Runtime: 26 ms, Memory: 18.8 MB
- TC: $O(n), where $n$ is the length of `nums`.
- SC: $O(1)$

<br>

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_jump = False
        gap = 0

        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= gap:
                can_jump = True
                gap = 1
            else:
                can_jump = False
                gap += 1

        return can_jump

```


### Iterating from the beginning

We only keep track of the maximum reachable index `maxReach`. `curr_idx`, which indicates the current index in `08_12_2025.py`, is actually not necessary, as we can use the loop index `i` directly.

- [Submission](https://leetcode.com/problems/jump-game/submissions/1732338600/)
- Runtime: 11 ms, Memory: 18.6 MB
- TC: $O(n)$
- SC: $O(1)$

<br>

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i, jump in enumerate(nums):
            if i > maxReach:
                # If the current index is beyond the maximum reachable index, we are stuck.
                return False
            # Update the furthest index we can reach.
            maxReach = max(maxReach, i + jump)
            # If we can reach or exceed the last index, return True.
            if maxReach >= len(nums) - 1:
                return True

```
