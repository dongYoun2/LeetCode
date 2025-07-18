# submission: https://leetcode.com/problems/palindrome-number/submissions/1701500105/

# 3 min
# TC: O(n)
# SC:O(1)

# From LeetCode Top Interview 150 - Math

# i tried solving without using python slicing, but it still uses string conversion, which i think goes against the intended purpose of the problem. mathy solution can be found at https://leetcode.com/problems/palindrome-number/submissions/1459352638/.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        n: str = str(x)

        for i in range(len(n) // 2):
            if n[i] != n[-(i+1)]:
                return False

        return True
