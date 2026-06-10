# submission: https://leetcode.com/problems/subarray-product-less-than-k/submissions/2028988677/
# runtime: 91 ms (beats 10.84%), memory: 22.14 MB (beats 46.59%)
# 17 min

# TC: O(n), where n is the length of the `nums` array
# SC: O(1)


# chose from a neetcode "sliding window" category.

# this problem is similar to the "930. Binary Subarrays With Sum" problem, which i couldn't solve yesterday. the difference is that this problem looks for the value (product) less than target (`k`), whereas the problem "930" finds the value (sum) that exactly matches the target (`goal`). as we know that we can either use sliding window or prefix sum for the problem "930", we can also apply either of them to this problem with minor modification that we have to use binary search instead of hash table for this problem since we are looking for the value that is less than the target (`k`).

# but here, i used a sliding window technique. the main algorithm is the same as the `at_most(k)` function's logic described in the README.md of the problem "930 Binary Subarrays With Sum".

# cf.) glad that i solved this problem. probably bc i went through the problem "930"'s correct solution yesterday.


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1:
            return 0

        n = len(nums)
        l = 0
        ans = 0
        curr_product = 1
        for r in range(n):
            curr_product *= nums[r]

            while curr_product >= k:
                curr_product /= int(nums[l])
                l += 1

            if curr_product < k:
                ans += r-l+1 # window size
        
        return ans


# notes while solving:
# wind sz, window, subarrays ending with the window's last elem
# 1 [10] --> [10] 
# 2 [10 5] --> [10 5], [5]
# 2 [5 2] --> [5 2], [2]
# 3 [5 2 6] --> [5 2 6], [2 6], [6]
