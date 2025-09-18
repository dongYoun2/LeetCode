# submission: https://leetcode.com/problems/longest-consecutive-sequence/submissions/1775392644/
# runtime: 73 ms, memory: 33.3 MB
# this is actually wrong because the problem requires O(n) time complexity solution.

# 6 min
# TC: O(n log n + n) -> O(n log n)
# SC: O(1)


# in the beginning, i spent 30 min to think of the O(n) time complexity solution, but i couldn't come up with it. so, i just solved it with O(n log n). it's very straightforward the `nums` array is sorted.

# cf.) while thinking of the O(n) TC solution, i thought of using the hash map but i wasn't sure enough. i guess when i was solving on 04/27/2025, i knew that i had to use the hash map in advance, so i was able to stick to using the hash map, and spend quite a long time to figure out the O(n) TC solution.

# in practice or coding interviews, it's likely that i won't be able to know which algorithm to use in advance. so, it's important to quickly notice which approach is the best for the problem. will have to practice more.


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
