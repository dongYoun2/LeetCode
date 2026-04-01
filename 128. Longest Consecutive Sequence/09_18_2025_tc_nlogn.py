# submission: https://leetcode.com/problems/longest-consecutive-sequence/submissions/1775392644/
# runtime: 73 ms (beats 13.99%), memory: 33.31 MB (beats 91.85%)
# 6 min
# this is a wrong solution because the problem requires O(n) time complexity solution.

# TC: O(n log n + n) -> O(n log n)
# SC: O(1)


# in the beginning, i spent 30 min to think of the O(n) time complexity solution, but i couldn't come up with it. so, i just solved it with O(n log n). the problem becomes straightforward wheb the `nums` array is sorted.

# cf.) while thinking of the O(n) TC solution, i thought of using the hash map but i wasn't sure enough. however, when i was solving on 04/07/2025, since i knew which algorithm (hash map) to use in advance (because i chose the problem based on the algorithm type), i was able to just stick to the hash map and spend a long time.

# in practice or for coding interviews, it's likely that i won't be able to know which algorithm to use. so, it's important to quickly notice which algorithm or data strcture would be the best approach. need some more practice.


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums = list(set(nums))
        nums.sort()
        ans = curr_len = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr_len += 1
                ans = max(ans, curr_len)
            else:
                curr_len = 1

        return ans
