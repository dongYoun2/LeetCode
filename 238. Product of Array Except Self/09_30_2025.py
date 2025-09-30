# submission: https://leetcode.com/problems/product-of-array-except-self/submissions/1787606796/
# runtime: 30 ms, memory: 25.91 MB

# 6 min
# TC: O(n), where n is the length of the `nums` array
# SC: O(n), for the `prefix` and `suffix` arrays


# the main idea is to compute the prefix product array by one forward pass, and the suffix product array by one backward pass.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        suffix = [1] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        return [a*b for a, b in zip(prefix, suffix)]
