[Problem](https://leetcode.com/problems/longest-increasing-subsequence/description/)




## Dynamic Programming


Refer to the `03_31_2025.py` solution for details.
<br>




## Greedy (Patience Sorting-based)

For this greedy (patience sorting idea) approach, we can first use linear search, then optimize with binary search. The binary search part solves the **follow-up question**, which requires to solve in $O(n \log n)$ time.

One important thing to note is that the `tails` array in the codes below **does not necessarily store an actual increasing subsequence**. It stores the smallest possible tail for each subsequence length, which is enough to compute the correct LIS length. 

To build an actual subsequence, we need extra bookkeeping, such as storing **previous index in the LIS chain** and **index in nums of the current tail** (instead of `tails` array itself). These are implemented in the [Build an actual Increasing Subsequence](#build-an-actual-increasing-subsequence) section, which includes `prev` and `tails_idx` arrays.
<br>

### Linear Search

[Submission](https://leetcode.com/problems/longest-increasing-subsequence/submissions/1957849556/)—Runtime: 15 ms (beats 72.38%), Memory: 19.16 MB (beats 99.75%)


```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tails = [nums[0]]
        
        for i in range(1, n):
            if nums[i] > tails[-1]:
                tails.append(nums[i])
            else:
                # Find the first element in tails that is greater than or equal to nums[i]
                k = 0
                while nums[i] > tails[k]:
                    k += 1
                tails[k] = nums[i]

        return len(tails)

```
cf.) The logic is the same as the Editorial's Approach 2: Intelligently Build a Subsequence.
<br>

### Binary Search

As mentioned above, greedy (patience sorting idea) + binary search solves the **follow-up question**.


- TC: $O(n \log n)$
- SC: $O(n)$
These complexiy analysis is the same throughout the binary search part.


[Submission](https://leetcode.com/problems/longest-increasing-subsequence/submissions/1957852994/)—Runtime: 11 ms (beats 77.97%), Memory: 19.44 MB (beats 76.38%)


```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(arr, target):
            l, r = 0, len(arr) - 1

            while l <= r:
                m = l + (r - l) // 2

                if arr[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            
            return l

        tail = []
        for num in nums:
            i = binary_search(tail, num)

            if i == len(tail):  # If num is greater than any element in tail
                tail.append(num)
            else:   # Otherwise, replace the first element in tail greater than or equal to num
                tail[i] = num
        
        return len(tail)

```
<br>


[Submission](https://leetcode.com/problems/longest-increasing-subsequence/submissions/1957853756/)—Runtime: 2 ms (beats 96.14%), Memory: 19.34 MB (beats 93.32%)


```python
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        for num in nums:
            i = bisect.bisect_left(tail, num)

            if i == len(tail):  # If num is greater than any element in tail
                tail.append(num)
            else:   # Otherwise, replace the first element in tail greater than or equal to num
                tail[i] = num
        
        return len(tail)

```
cf.) This code is similar to the Editorial's Approach 3: Improve With Binary Search.
<br>


#### Build an actual Increasing Subsequence



[Submission](https://leetcode.com/problems/longest-increasing-subsequence/submissions/1957804547/)—Runtime: 52 ms (beats 70.14%), Memory: 19.51 MB (beats 51.50%)

```python
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        tails_idx = []       # indices of smallest tail for each length
        prev = [-1] * n      # prev[i] = previous index in LIS ending at i

        for i, num in enumerate(nums):
            # use bisect on values via a helper list
            vals = [nums[idx] for idx in tails_idx]
            pos = bisect.bisect_left(vals, num)

            if pos > 0:
                prev[i] = tails_idx[pos - 1]

            if pos == len(tails_idx):
                tails_idx.append(i)
            else:
                tails_idx[pos] = i

        # reconstruct LIS
        lis = []
        k = tails_idx[-1]
        
        while k != -1:
            lis.append(nums[k])
            k = prev[k]

        lis.reverse()

        # actual increasing subsequence
        print(lis)
        
        return len(lis)

```