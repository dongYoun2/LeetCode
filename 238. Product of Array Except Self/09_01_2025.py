# submission: https://leetcode.com/problems/product-of-array-except-self/submissions/1756369500/
# runtime: 31 ms, memory: 26 MB

# 7 min
# TC: O(n), where n is the length of nums
# SC: O(n)


# From LeetCode Top Interview 150 - Array / String

# the problem is an application of prefix sum technique. pretty straightforward once you notice this is a prefix sum problem. One optimization could be reducing the space complexity to O(1) by using only the output array to store the prefix products and using a single variable to keep track of the suffix product, which solves the follow-up question. optimized code can be found in https://leetcode.com/problems/product-of-array-except-self/submissions/1570581293/.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cum_prod = [1] * n
        cum_prod_reversed = [1] * n

        for i in range(1, n):
            cum_prod[i] = cum_prod[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            cum_prod_reversed[i] = cum_prod_reversed[i+1] * nums[i+1]

        return [a * b for a, b in zip(cum_prod, cum_prod_reversed)]
