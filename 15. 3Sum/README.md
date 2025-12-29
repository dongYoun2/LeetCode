This README provides other approaches apart from `03_25_2025.py` solution.

- [Two-pointer Approach](#two-pointer-approach)
  - [No Optimization](#no-optimization)
  - [With Optimization](#with-optimization)
- [Hash-based Nested Two-sum Approach](#hash-based-nested-two-sum-approach)
- [Dividing Cases Approach](#dividing-cases-approach)


## Two-pointer Approach

### No Optimization

In the code below, note that submission will fail if we use the `list` for the `ans` variable.

- TC: $O(n^2)$
- SC: $O(\log n)$ (for built-in sorting)
- [submission result](https://leetcode.com/problems/3sum/submissions/1586248590/) (Runtime: 1482 ms, Memory: 20.17 MB)

Here, the two-sum part algorithm is the same as the [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted) solution.

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # for two-pointer alg.

        ans = set()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            target = -nums[i]   # finding nums[l] + nums[r] == target

            while l < r:    # two-sum part
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

        return list(ans)
```

### With Optimization

There are two helpful optimizations:
1. Early return if the current number (i.e. `nums[i]`) is positive. (with only this optimization, runtime is 1374 ms)
2. Skipping the already checked smallest number (i.e. `nums[i-1] == nums[i]`). (with only this optimization, runtime is 584 ms)

Though the time complexity is still $O(n^2)$ (same as the [No Optimization](#no-optimization) code), but the runtime is significantly reduced in practice.

cf.) We can also skip the middle and largest numbers (i.e. `while l < r and nums[l] == nums[l+1]` and `while l < r and nums[r] == nums[r-1]`), but it's not worthwhile. The runtimes are similar (< 10 ms difference) as the below submission.

- TC: $O(n^2)$
- SC: $O(\log n)$
- [submission result](https://leetcode.com/problems/3sum/submissions/1868809258/) (Runtime: 410 ms, Memory: 19.63 MB)

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # for two-pointer alg.

        ans = set()
        for i in range(len(nums)):
            if nums[i] > 0: # optimization 1: early return
                break

            if i != 0 and nums[i-1] == nums[i]: # optimization 2: skipping previously checked smallest number
                continue

            l, r = i + 1, len(nums) - 1
            target = -nums[i]   # finding nums[l] + nums[r] == target

            while l < r:    # two-sum part
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

        return list(ans)
```

## Hash-based Nested Two-sum Approach

- TC: $O(n^2)$
- SC: $O(n)$ (hash table (set))
- [submission result](https://leetcode.com/problems/3sum/submissions/1586249261/) ((Runtime: 785 MB ms, Memory: 23.30 MB))

Here, the two-sum part is very similar to the LeetCode 2Sum question except for using **set** instead of **dictionary** since we need value itself rather than the index.

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        dups = set()
        for i in range(len(nums)):
            if nums[i] in dups: # prevent when the array contains many repeated values (without this, TLE occurs for the test case with 3,000 zeros)
                continue

            dups.add(nums[i])
            target = - nums[i]

            cands = set()
            for j in range(i+1, len(nums)): # two-sum part
                if target - nums[j] in cands:
                    tup = tuple(sorted([nums[i], nums[j], target - nums[j]]))   # target - nums[j] == - (nums[i] + nums[j])
                    ans.add(tup)

                cands.add(nums[j])

        return list(ans)
```


## Dividing Cases Approach

This approach is straightforward and easy to understand. Please refer to either `03_25_2025.py` or `09_10_2025_dividing_cases.py` for the details.