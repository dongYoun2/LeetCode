# submission: https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/2020519107/
# runtime: 200 ms (beats 93.28%), memory: 30.82 MB (beats 46.31%)
# 31 min ("06_02_2026_TLE.py" time included)
# solved with a sliding window approach (optimized version)

# TC: O(n log n + n) -> O(n log n)
# SC: O(n) (sorting)


# chose from a neetcode "sliding window" category.

# as an extension of the "06_02_2026_TLE.py" solution, i optimized the per-window computation. instead of iterating over all elements in the window, we can simply update the change in cost caused by the new target value in O(1) time.

# another thing to notice is that we increment `left` by either 1 or 0 per iteration unlike typical variable-size sliding window approaches (refer to the "Editorial's Approach 1: Sliding Window" for a typical implementation). this is because we only care about the length of the window, specifically the maximum possible window length. therefore, instead of using loop to shrink the window (or increment the `left` pointer), we can use `if` statement so that the window size never decreases throughout the algorithm, which makes more efficient in practice. this also means that window size always represents the maximum possible window length we have found so far (this is why `assert ans == n - left` at the end is `True` in the code below). 

# cf.) the logic is identical to the "Editorial's Approach 2: Advanced Sliding Window." The only difference is that we decreased and increased the variable `k` as needed in the solution below, whereas the editorial solution maintains the `curr` variable to keep track of the sum of the elements in a current window.


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 1
        left = 0
        for right in range(1, n):
            k -= (nums[right] - nums[right-1]) * (right - left)
            
            if k >= 0:
                ans = max(ans, right-left+1)
            else:
                k += nums[right] - nums[left]
                left += 1
        
        # assert ans == n - left
        return ans

# notes while solving:
# expected TC: n log n + n ?
