[Problem](https://leetcode.com/problems/binary-subarrays-with-sum/)

I chose this problem from a neetcode "sliding window" category, so I simply approached with the sliding window technique, as shown in the `06_09_2026_wrong.py` and `06_09_2026_tle.py` solutions. However, easier solution to think of and to implement is using prefix sum and hash table.


## Prefix Sum + Hash Table

We can transform this problem into finding two prefix sums whose difference equals to `goal` (same as the Hint 1 in the problem statement). Since the prefix sum array is non-decreasing (or monotonically increasing), we can track the previous values that are less than or equal to the current value while iterating through the prefix sum array.


[Submission](https://leetcode.com/problems/binary-subarrays-with-sum/submissions/2029069789/)—Runtime: 27 ms (beats 92.21%), Memory: 23.27 MB (beats 11.57%)

- TC: $O(n)$, where $n$ is the length of `nums`
- SC: $O(n)$ (for the hash table)


```python
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1

        prefix_sum = 0
        ans = 0

        for num in nums:
            prefix_sum += num

            # Need previous prefix_sum:
            # prefix_sum - previous = goal
            # previous = prefix_sum - goal
            ans += count[prefix_sum - goal]

            count[prefix_sum] += 1

        return ans

```



## Sliding Window

We have seen the critical issue mentioned in the `06_09_2026_wrong.py` solution. If we think of finding the number of subarrays with sum less than or equal to the target value (`goal`), we can apply the standard variable-size sliding window technique. Then, how can we find the number of subarrays with sum exactly equal to `goal`?

The solution is applying the sliding window twice. We can first find the number of subarrays with sum at most `goal`, and then subtract the number of subarrays with sum at most `goal - 1` from it. Let function `at_most(k)` return the number of subarrays with sum at most `k`. Then, the answer is `at_most(goal) - at_most(goal - 1)`.

One thing to note is why are we incrementing the `count` by **window size** (`right - left + 1`) every iteration, not by 1? This value (window size) represents the number of subarrays that includes the rightmost element of the current window as the last element. We don't need to count all the subarrays that can be formed with any values in the current window because we have already counted them from the previous iterations. More detailed explanation with the example can be found [here](https://leetcode.com/problems/binary-subarrays-with-sum/editorial/comments/2299682/?parent=2299534).


[Submission](https://leetcode.com/problems/binary-subarrays-with-sum/submissions/2029070211/)—Runtime: 39 ms (beats 34.15%), Memory: 20.03 MB (beats 76.86%)

- TC: $O(n)$
- SC: $O(1)$


```python
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(k: int) -> int:
            if k < 0:
                return 0

            left = 0
            window_sum = 0
            count = 0

            for right in range(len(nums)):
                window_sum += nums[right]

                while window_sum > k:
                    window_sum -= nums[left]
                    left += 1

                count += right - left + 1

            return count

        return at_most(goal) - at_most(goal - 1)

```