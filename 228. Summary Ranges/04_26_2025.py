# problem: https://leetcode.com/problems/summary-ranges/
# submission: https://leetcode.com/problems/summary-ranges/submissions/1618918134/

# 7 min
# TC: O(n), where n is the length of nums
# SC: O(1) (not counting the output)


# From LeetCode Top Interview 150 - Intervals


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []

        ans = []
        start = end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
                continue

            range_ = str(start) if start == end else f"{start}->{end}"
            ans.append(range_)

            start = end = nums[i]

        range_ = str(start) if start == end else f"{start}->{end}"
        ans.append(range_)

        return ans
