# problem: https://leetcode.com/problems/longest-consecutive-sequence/
# submission: https://leetcode.com/problems/longest-consecutive-sequence/submissions/1600133520/ (includes test case for memory limit exceeded)

# 15 min
# TC: O(n + R), where n is the number of elements in nums, and R is the range of numbers in nums (computed as max(nums) - min(nums))
# SC: O(R)

# Knew that I had to use hash map since I am solving problems based on the algorithm type.

# In the below code, if the range of numbers in nums is small, then the time complexity is very close to O(n), which meets the requirement of the problem. However, if the R is large, this solution is inefficient in terms of both time and space complexity. Concretely, a test case where nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10**6] will take a lot of time and memory to run.

# cf.) This is just like the problem of counting sort. Counting sort is a sorting algorithm that is efficient when the range of numbers in the input array is small since it uses range-based auxiliary array.


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        min_n, max_n = min(nums), max(nums)
        table = [False] * (max_n - min_n + 1)

        convert_idx = lambda idx: idx - min_n

        table[convert_idx(min_n)] = table[convert_idx(max_n)] = True

        for n in nums:
            table[convert_idx(n)] = True

        ans = consecutive_cnt = 0
        for elem in table:
            if elem:
                consecutive_cnt += 1
                ans = max(ans, consecutive_cnt)
            else:
                consecutive_cnt = 0

        return ans
