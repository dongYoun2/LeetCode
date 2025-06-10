# submission: https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/1659211053/

# 64 min (including the time for "06_09_2025_brute_force.py")

# Still a wrong solution even after looking at all the hints listed on the problem page. The flattened array constructed by simply appending the original array (last element excluded) to itself. To find the maximum sum of a circular subarray, it is not enough to simply remove the left-most element when the buffer size reaches full. We may need to remove multiple elements from the left side.

# Counter example: [100, -7, -7, 2, -7, -7, 100]


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        nums_flatten = nums + nums[:n-1]

        print(nums_flatten)

        ans = curr_sum = nums_flatten[0]
        left = right = 0
        for i in range(1, len(nums_flatten)):
            right = i
            if nums_flatten[i] >= curr_sum + nums_flatten[i]:
                curr_sum = nums_flatten[i]
                left = i
            else:
                curr_sum += nums_flatten[i]

            ans = max(ans, curr_sum)

            if right - left + 1 >= n:
                curr_sum -= nums_flatten[left]
                left += 1
                ans = max(ans, curr_sum)

        return ans
