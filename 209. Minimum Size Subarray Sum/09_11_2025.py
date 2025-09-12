# submission: https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1767706882/
# runtime: 11 ms, memory: 28.3 MB

# 18 min
# TC: O(n), where n is the length of nums
# SC: O(1)


# From LeetCode Top Interview 150 - Sliding Window

# second time solving this problem. took longer than the first time i solved it. also, i knew that i had to use the sliding window technique beforehand. though, there are some unneccessary (or duplicate codes) in the code below. better solution can be found in the README file.


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        s = e = 0
        curr_sum = 0
        curr_len = 0
        ans = float('inf')

        while e < n:
            curr_sum += nums[e]
            if curr_sum >= target:
                curr_len = e - s + 1
                ans = min(ans, curr_len)

                while curr_sum >= target:
                    curr_len = e - s + 1
                    ans = min(ans, curr_len)
                    curr_sum -= nums[s]
                    s += 1

            e += 1

        return 0 if ans == float('inf') else ans
