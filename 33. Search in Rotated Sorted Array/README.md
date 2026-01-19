[Problem](https://leetcode.com/problems/search-in-rotated-sorted-array/)

The **key idea** for this problem is that at any midpoint, one half is always sorted. So, we need to check which half is sorted, then decide if target must lie inside it or the other half.


Note that when checking whether the left half is sorted (or the pivot is in the right part), we need the equality in the `if` condition (i.e. `if nums[l] <= nums[m]: ...`). This is because we are using the floor division to compute the middle index, which makes `m == l` possible. If we had used the ceiling division, `nums[l] < nums[m]` would be fine but need equality in the right half sort check (i.e. `nums[m] <= nums[r]`).


- [Submission](https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1820843396/) (Runtime: 0 ms, Memory: 18.02 MB)
- TC: $O(\log n)$, where $n$ is the number of elements in the array.
- SC: $O(1)$

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            # equality must exist here. if not, "test case: nums = [3, 1], target = 1" fails.
            if nums[l] <= nums[m]:  # pivot is in the right part
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:   # pivot is in the left part
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1

```


The code below is almost equivalent to the above code, but the below checks whether the right half is sorted (or the pivot is in the left part) first. In this case, note that we don't need the equality in the `if` condition (i.e. `if nums[m] < nums[r]: ...`).

The reason that we need equality when we check if the pivot is in the right half first (above) and not when we check if the pivot is in the left half first (below) is because we are using the **floor division** to compute the middle index (i.e. `m = (l + r) // 2`). So, for the two elements case where the middle index is the same as the left index, we need to check if the left element is less than or **equal to** the middle element to determine if the pivot is in the right part, which if this is true, the pivot is the same as the right element.

So the **takeaway** is always consider the edge cases, such as where the number of elements is 1 or 2.

- [Submission](https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1820842896/) (Runtime: 0 ms, Memory: 18.09 MB)
- Complexity analysis is the same as the above code.

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            # when comparing nums[m] and nums[r], equality is not needed (unlike the nums[m] and nums[l] comparison)
            if nums[m] < nums[r]:   # pivot is in the left part
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:    # pivot is in the right part
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1


        return -1

```