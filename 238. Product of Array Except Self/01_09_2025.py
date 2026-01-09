# submission: https://leetcode.com/problems/product-of-array-except-self/submissions/1880190011/
# runtime: 27 ms, memory: 25.5 MB

# 5 min
# TC: O(n), where n is the length of the input array
# SC: O(1) (output array is not counted)


# unlike "09_01_2025.py" and "09_30_2025.py", this solution has a constant space complexity because we used the output array to store the prefix products and one single `tmp` variable to store the suffix product on the fly.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for _ in range(n)]
        
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        
        tmp = 1
        for i in range(n - 2, -1, -1):
            tmp *= nums[i+1]
            ans[i] *= tmp
        
        return ans
