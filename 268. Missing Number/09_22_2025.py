# submission: https://leetcode.com/problems/missing-number/submissions/1779223642/
# runtime: 0 ms, memory: 18.91 MB

# 2 min
# TC: O(n), where n is the length of nums
# SC: O(1)


# the solution below directly solves the follow-up question. the idea is that we learned from high school math that the sum of the first n natural numbers is n * (n + 1) / 2. so, we can just subtract the sum of the input array from the sum of the first n natural numbers.

# there are many other solutions to solve this problem, but this one is the most optimal (along with the bit manipulation solution) in terms of both time and space complexity. for more details, refer to the README file.


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        all_sum = int(n * (n + 1) / 2)

        return all_sum - sum(nums)
