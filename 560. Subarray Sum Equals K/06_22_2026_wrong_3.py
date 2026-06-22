# didn't submit this solution since i could find the wrong test case beforehand
# 50 min (time including "06_22_2026_wrong.py" and "06_22_2026_wrong_2.py")


# this code is similar to the solutions for the problems the problems "930. Binary Subarrays With Sum" and "713. Subarray Product Less Than K". actually, tihs code is correct when the input integers are non-negative.

# however, since inputs and `k` can be negative, we need to use prefix sum + hash table approach similar to the solution described in the README of the problem "930. Binary Subarrays With Sum".


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)


        def at_most(goal):
            left = 0
            curr_sum = 0
            cnt = 0

            for right in range(n):
                curr_sum += nums[right]
                
                while left < right and curr_sum > goal:
                    curr_sum -= nums[left]
                    left += 1

                if curr_sum <= goal:
                    cnt += right-left+1
                
            return cnt
        

        return at_most(k) - at_most(k-1)
