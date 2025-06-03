# submissioin: https://leetcode.com/problems/maximum-subarray/submissions/1652225437/

# After implementing "06_02_2025_follow_up_wrong_1.py" and with the help of ChatGPT, I realized that the maximum subarray that crosses the midpoint does not necessarily include the maximum subarrays from both halves. Instead, it can be formed by taking the best suffix from the left half and the best prefix from the right half. However, I still struggled to implement the correct logic as shown in the code below.

# Greedily expanding from the midpoint by always choosing the larger immediate neighbor is incorrect because the optimal crossing subarray may require taking a smaller next element first to reach a larger overall suffix or prefix; in other words, choosing between nums[s-1] and nums[e+1] based solely on which is bigger can miss a combination of elements whose total sum exceeds any single-step choice.

# Below is the counter example that demonstrates the flaw in the greedy approach:

# nums = [ -2, -2, -1,  -2,  -2,  -2,   3 ]
#           0   1   2    3    4    5    6
# left half = [0..3], right half = [4..6], mid = 3

# Correct cross:
#   best_left_suffix  = max([-2],[-1,-2],[-2,-1,-2],[-2,-2,-1,-2]) = -2
#   best_right_prefix = max([-2],[-2,-2],[-2,-2,3]) = -1
#   cross = -2 + -1 = -3

# Greedy pick:
#   start s=3(e=-2), e=4(-2), curr=-4, pick larger of nums[2]=-1 vs nums[5]=-2 → add -1 → curr=-5
#   then compare nums[1]=-2 vs nums[5]=-2 → add -2 → curr=-7
#   then compare nums[1]=-2 vs nums[6]=3 → add 3 → curr=-4; final cross_max = -4 (wrong)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        assert len(nums) > 0

        def merge(arr1_max_sum, arr1_start, arr1_end, arr2_max_sum, arr2_start, arr2_end):
            assert arr1_start <= arr1_end and arr2_start <= arr2_end

            s, e = arr1_end, arr2_start
            cross_max_sum = curr_sum = nums[s] + nums[e]

            while arr1_start < s and e < arr2_end:
                if nums[s-1] > nums[e+1]:
                    s -= 1
                    curr_sum += nums[s]
                else:
                    e += 1
                    curr_sum += nums[e]

                cross_max_sum = max(cross_max_sum, curr_sum)

            if s == arr1_start:
                while e < arr2_end:
                    e += 1
                    curr_sum += nums[e]
                    cross_max_sum = max(cross_max_sum, curr_sum)
            elif e == arr2_end:
                while s > arr1_start:
                    s -= 1
                    curr_sum += nums[s]
                    cross_max_sum = max(cross_max_sum, curr_sum)

            return max([arr1_max_sum, arr2_max_sum, cross_max_sum])


        def compute_max_sum(start, end):
            if start == end:
                return nums[start]

            arr1_start, arr1_end = start, (start + end) // 2
            arr2_start, arr2_end = arr1_end + 1, end

            arr1_max_sum = compute_max_sum(arr1_start, arr1_end)
            arr2_max_sum = compute_max_sum(arr2_start, arr2_end)

            max_sum = merge(arr1_max_sum, arr1_start, arr1_end, arr2_max_sum, arr2_start, arr2_end)

            return max_sum

        return compute_max_sum(0, len(nums) - 1)
