[Problem](https://leetcode.com/problems/gas-station/)


## Greedy Solution

Unlike `09_09_2025.py`, `curr_gas` is always added by the amount of `gas[i] - cost[i]` (`tank[i]` in `09_09_2025.py`) in the loop. The below loop logic is much cleaner than that of `09_09_2025.py`.


- [Submission](https://leetcode.com/problems/gas-station/submissions/1571506849/) (Runtime: 11 ms, Memory: 23.2 MB)
- TC: $O(n)$, where $n$ is the length of `gas` (or `cost`)
- SC: $O(1)$

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start_idx = curr_gas = 0
        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                start_idx = i + 1
                curr_gas = 0

        return start_idx

```