[Problem](https://leetcode.com/problems/longest-consecutive-sequence/description/)

## Hash Map Solution

- [Submission](https://leetcode.com/problems/longest-consecutive-sequence/submissions/1775443954/) (Runtime: 43 ms, Memory: 33.3 MB)
- TC: $O(n)$, where $n$ is the number of elements in `nums`
- SC: $O(n)$ (`num_set`)

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)       # Unique numbers for O(1) lookup
        longest_streak = 0

        for num in num_set:
            # Start only if it's the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

```

## Sorting Solution

Please refer to `09_18_2025_tc_nlogn.py` for the solution.
