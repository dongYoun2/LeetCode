# problem: https://leetcode.com/problems/combinations/
# submission: https://leetcode.com/problems/combinations/submissions/1637008691/

# 1 min
# runtime: 17 ms, memory: 56.9 MB
# TC: O(k \cdot \binom{n}{k}$ ($\binom{n}{k} (same as the code in "fully_pruned_backtracking.md")
# SC: O(n + k) -> O(k). O(n) for the list of numbers from 1 to n, and O(k) for the `combinations` iterator.

# From LeetCode Top Interview 150 - Backtracking

# Since Python has the `combinations` function in the `itertools` module, simply using that is the most efficient and easiest way to solve this problem, although the intention of the problem is to implement a backtracking solution.


from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = combinations(list(range(1, n+1)), k)

        return list(combs)