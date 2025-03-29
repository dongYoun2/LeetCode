## Finding Peak Element Using Binary Search

#### Early Return for Edge Cases

- [Submission](https://leetcode.com/problems/find-peak-element/submissions/1590268618/)
- Remove some if-else statements in the while loop from `03_29_2025.py` by early returning for the edge cases.

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:  # array with a single element
            return 0

        if nums[0] > nums[1]:   # check if the first element is the peak element
            return 0

        if nums[-1] > nums[-2]: # check if the last element is the peak element
            return len(nums) - 1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2 # prevent overflow

            if nums[m-1] < nums[m] and nums[m] > nums[m+1]: # found peak index
                return m
            elif nums[m-1] > nums[m]:
                r = m - 1
            elif nums[m+1] > nums[m]:
                l = m + 1

```
<br>

#### LeetCode Editoral's **Approach 3: Iterative Binary Search**

- Removing equality from the while loop's inequality condtion on `03_29_2025.py` allows us to only consider whether the right neighbor is smaller than the current element (`nums[mid]`). Also, right pointer update rule has to be slightly changed (`r = mid`).
- Plus, I just found out that in python, we don't need to worry about integer overflow when using `(l + r) // 2` becuase python internally handles large integers unlike other languages like C++.

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
```