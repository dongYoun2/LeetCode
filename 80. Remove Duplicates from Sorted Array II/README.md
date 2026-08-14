[Problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)


## Two-pointer Approach (Concise and Optimized Version)

This solution is optimized version of the solution `08_06_2025.py`. By always keeping track of the count of duplicates, we can ensure that we only keep up to two occurrences of each number in the sorted array.

So the first logics (first `if-else` block) computes the count of duplicates of current number, and the second logic (second `if` block) updates the current number to the propoer next position for the modified array if the condition is satisfied.

[Submission](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/submissions/1565609944/)—Runtime: 83 ms (beats 77.07%), Memory: 20.51 MB (beats 100.00%)


- TC: $O(n)$, where $n$ is the length of the input array.
- SC: $O(1)$


```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        pos = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1

            if cnt <= 2:
                nums[pos] = nums[i]
                pos += 1

        return pos

```