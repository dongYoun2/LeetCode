# Spent almost an hour solving the follow-up question, but the solution is still wrong. The divid and conquer structure is correct, but the merging logic is flawed. The `merge(...)` function in the code below assumes that the best crossing subarray always includes the best “anywhere” segment from each half, which is not necessarily true. This is because those optimal subarrays might not touch the midpoint. In contrast, a valid crossing subarray must consist of a suffix ending exactly at mid and a prefix starting exactly at mid+1, neither of which is guaranteed to coincide with the globally best subarray in each half.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        assert len(nums) > 0

        def merge(arr1_max_sum, arr1_max_start, arr1_max_end, arr2_max_sum, arr2_max_start, arr2_max_end):
            merged_max_sum = arr1_max_sum + arr2_max_sum + sum(nums[arr1_max_end+1:arr2_max_start])

            max_sum = max([arr1_max_sum, arr2_max_sum, merged_max_sum])

            if max_sum == merged_max_sum:
                return max_sum, arr1_max_start, arr2_max_end
            elif max_sum == arr1_max_sum:
                return arr1_max_sum, arr1_max_start, arr1_max_end
            elif max_sum == arr2_max_sum:
                return arr2_max_sum, arr2_max_start, arr2_max_end


        def compute_max_sum(start, end):
            if start == end:
                return nums[start], start, end

            arr1_start, arr1_end = start, (start + end) // 2
            arr2_start, arr2_end = arr1_end + 1, end


            arr1_max_sum, arr1_max_start, arr1_max_end = compute_max_sum(arr1_start, arr1_end)
            arr2_max_sum, arr2_max_start, arr2_max_end = compute_max_sum(arr2_start, arr2_end)

            return merge(arr1_max_sum, arr1_max_start, arr1_max_end, arr2_max_sum, arr2_max_start, arr2_max_end)


        return compute_max_sum(0, len(nums) - 1)[0]
