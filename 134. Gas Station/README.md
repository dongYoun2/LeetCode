[Problem](https://leetcode.com/problems/gas-station/)


## Greedy Solution

Unlike `09_09_2025.py`, `curr_gas` is always added by the amount of `gas[i] - cost[i]` (`tank[i]` in `09_09_2025.py`). This is cleaner than `09_09_2025.py`'s logic. While this code early returns (with two passes) for impossible case, `03_05_2026.py` solves the problem with a single pass (no early return). 


- [Submission](https://leetcode.com/problems/gas-station/submissions/1571506849/)—Runtime: 11 ms (Beats 99.61%), Memory: 23.23 MB (Beats 100.00%)
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