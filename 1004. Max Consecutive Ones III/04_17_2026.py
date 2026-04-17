# submission: https://leetcode.com/problems/max-consecutive-ones-iii/submissions/1980925028/
# runtime: 63 ms (beats 43.26%), memory: 22.03 MB (beats 88.32%)
# 30 min

# TC: O(n)
# SC: O(1)


# chose the problem from the "sliding window" category.

# though i knew this is a sliding window problem, spent a bit of time to think about the logic. instead of sliding window technique, i also thought of saving the first and last index of all subarrays with the consecutive ones. however, i couldn't think of how to proceed after that.

# with the sliding window technique, the algorithm is as follows:
# 1. expand the window by one by including the current element.
# 2. if the number of zeros in the current window is greater than `k`, shrink the window until the number of zeros is less than or equal to `k`.
# 3. update the answer with the size of the current window.

# cf.) the code below also keep track of the frequency of ones in a current window. i first thought of this, but it's unnecessary because we only want the number of zeros to flip to be less than or equal to `k`. so, we can simply keep the frequency of zeros only. (better code submission: https://leetcode.com/problems/max-consecutive-ones-iii/submissions/1980938507/)

# cf.) Brute force solution would be trying all subarrays and check if the number of zeros to flip to be less than or equal to `k`. this would take O(n^2) time.


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        left = 0
        one_freq = zero_freq = 0
        for right in range(n):
            if nums[right] == 1:
                one_freq += 1
            else:
                zero_freq += 1
            
            while zero_freq > k:
                if nums[left] == 1:
                    one_freq -= 1
                else:
                    zero_freq -= 1
                left += 1
            
            window_sz = right - left + 1
            ans = max(ans, window_sz)

        return ans
