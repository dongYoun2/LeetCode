# submission: https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1820817584/
# test case "nums = [3, 1], target = 1" fails

# 75 min

# spent 75 min to code this up, but fails on the above mentioned test case. the only problem in this code is that the equality is missing in the codition `if nums[l] < nums[m]:`. the correct code can be found here: https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1820833263/.

# the reasoning behind we need the equality when checking if the left half is sorted is because we are using the floor division to compute the middle index, which makes `m == l` possible. if we had used the ceiling division, `nums[l] < nums[m]` would be fine but need equality in the right half sort check (i.e. `nums[m] <= nums[r]`).

# though after adding the equality in the above condition, the code contains duplicates. there exists a same sort half checks in both the first if block and the else block. this is because we are first branching based on whether the target is larger or smaller than the middle value, and this is unnecessary.

# more optimized implementation can first branch based on determining which half is sorted, which is a direct geometric property of a rotated sorted array. for more details, refer to the markdown file.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            if target > nums[m]:
                if nums[m] < nums[r]:   # right half is sorted (pivot is in the left half)
                    if nums[m] < target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                else:   # left half is sorted (pivot is in the right half)
                    if nums[l] <= target < nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
            else:   # target < nums[m]
                if nums[l] < nums[m]:   # left half is sorted (pivot is in the right half)
                    if nums[l] <= target < nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
                else:   # right half is sorted (pivot is in the left half)
                    if nums[m] < target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1

        return -1
