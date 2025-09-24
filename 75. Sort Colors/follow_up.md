[Problem](https://leetcode.com/problems/sort-colors/)

This is a [Dutch National Flag Problem](https://en.wikipedia.org/wiki/Dutch_national_flag_problem).


## Two-pointer Approach (One-pass)

The core idea is to push all 0s to the left and all 2s to the right. so we can easily notice that we need two pointers, `left` and `right`, to keep track of the positions of 0s and 2s, respectively.

One caveat is that when current element (nums[curr]) is 0, we also need to swap it with the element at `left` pointer because the element at `left` pointer is guaranteed to be either 0 or 1.


- [Submission](https://leetcode.com/problems/sort-colors/submissions/1780752255/)
- TC: O(n), where n is the number of elements in nums
- SC: O(1)


```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, curr, right = 0, 0, len(nums) - 1

        while curr <= right:
            if nums[curr] == 0:  # case: 0 -> send to front
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:    # case: 2 -> send to back
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:   # case: 1 -> leave in middle
                curr += 1

```

cf.) When `left` and `curr` are the same, we actually don't need to swap, because it means they are both 0s, but simply swapping doesn't make any difference.

so to make the first `if` block more precise (case 0 -> send to front), we can also write it as the below snippet:

```python
if nums[curr] == 0:  # case: 0 -> send to front
    if curr != left:
        nums[left], nums[curr] = nums[curr], nums[left]
    left += 1
    curr += 1
```

[submission](https://leetcode.com/problems/sort-colors/submissions/1780752382/)