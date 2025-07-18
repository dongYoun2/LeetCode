# submission: https://leetcode.com/problems/sqrtx/submissions/1702629092/
# runtime: 3 ms, memory: 17.8 MB

# 7 min
# TC: O(log (n // 2)) -> O(log n), where n is the input number x
# SC: O(1)

# From LeetCode Top Interview 150 - Math

# after submitting the linear time solution (07_18_2025.py), I noticed that the execution time took quite long. i looked at the topic tags and realized that this problem can be also solved using binary search. so i implemented using the binary search.

# clues to note that the problem is a binary search problme:
# 1. monotonic behavior: function or a sequence either increases or decreases
# 2. searching for a value or threshold: smallest/largest/any value meeting a condition
# 3. input range: if n >= 10B (100억), the solution should likely be O(log n), and binary search is a well-known O(log n) algorithm
# 4. brute force is linear and slow


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x == 1: return 1

        l, r = 0, x // 2

        while l <= r:
            n = (l + r) // 2

            if n * n == x:
                return n
            elif n * n < x:
                l = n + 1
            else:
                r = n - 1

        return r
