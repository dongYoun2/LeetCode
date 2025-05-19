# submission: https://leetcode.com/problems/permutations/submissions/1638424156/

# 1 min
# runtime: 0 ms, memory: 17.8 MB
# TC: O(n*n!), where n is the length of `nums`. Python permutations module internally produces each permutation in O(n) time, and there are total n! permutations.
# SC: O(n). permutations iterator only holds the current processing permutation in memory.

# From LeetCode Top Interview 150 - Backtracking

# Although the problem intention is to use backtracking, using Python's built-in permutaitons function is the most concise and efficient way.


from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))