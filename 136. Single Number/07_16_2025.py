# submission: https://leetcode.com/problems/single-number/submissions/1700401362/
# runtime: 2 ms, memory: 19.6 MB

# 3 min
# TC: O(n), where n is the length of `nums`
# SC: O(1)

# From LeetCode Top Interview 150 - Bit Manipulation

# this is a third time solving this problem. the first and second time was on 04/04/2024 and 11/16/2024 respectively. i remember that i was shocked how this can be solved with XOR bitwise operation, which solves in linear time while using constant space.

from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = lambda a, b: a ^ b

        return reduce(xor, nums)
