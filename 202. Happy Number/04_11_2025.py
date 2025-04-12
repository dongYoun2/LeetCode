# problem: https://leetcode.com/problems/happy-number/
# submission: https://leetcode.com/problems/happy-number/submissions/1604142201/

# 9 min
# TC: O(c log n) -> O(log n), where c is a constant and log is base 10
# SC: O(1)

# From LeetCode Top Interview 150 - Hashmap

# Tbh, if I didn't know this problem was a hashmap problem, it would have taken a while to solve it. This is because I actually couldn't exactly prove that cycle must exist if I couldn't find a happy number.

# For more details, refer to the LeetCode Editorial section.

# cf.) The editorial section explicitly mentions the case where 'n' keeps increasing to infinity and explains why we don't need to consider this case. However, while I was solving the problem, I just assumed that 'n' couldn't increase to infinity and didn't consider this case. I will thoroughly review this question later.


class Solution:
    def isHappy(self, n: int) -> bool:
        set_ = set()

        while not n in set_:
            if n == 1:
                return True

            set_.add(n)
            temp = 0
            while n != 0:
                n, r = divmod(n, 10)
                temp += r ** 2

            n = temp

        return False


# notes while solving

# 4
# 16
# 37
# 58
# 25 + 64 = 89
# 64 + 81 = 145
# 1 + 16 + 25 = 42
# 16 + 4 = 20
# 4