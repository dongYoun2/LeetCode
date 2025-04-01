# problem: https://leetcode.com/problems/interleaving-string/
# submission: https://leetcode.com/problems/interleaving-string/submissions/1593583290/

# 31 min
# TC: O(n * m * (n + m)), where n and m are the lengths of s1 and s2 respectively (total n * m states, and each state has a string of length n + m (we are using string slicing))
# SC: O(n * m * (n + m) + (n+m)) -> O(n * m * (n + m)) (logic is the same as above with additional space for the recursion stack)

# Although I knew that I had to use the DP algorithm, this problem felt very difficult at first glance. I tried to think of it in a bottom-up approach but couldn't directly think of the recurrent relation. Then, I tried to think of the top-down approach just like the top-down DP solution of the "word break" problem. This way, coming up with the recurrent relation was pretty intuitive, and I was able to solve it. Meanwhile, I had an issue with the memoization, but I ended up using the `cache` decorator, which is a handy way to use the caching (or memoization) technique. (Tbh, I was surprised by myself after solving the problem lol.)


from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def interleaving(s, t, target):
            assert len(s) + len(t) == len(target)

            if target == "":
                return True

            for i in range(1, len(s) + 1):
                if s[:i] == target[:i]:
                    if interleaving(s[i:], t, target[i:]):
                        return True

            for i in range(1, len(t) + 1):
                if t[:i] == target[:i]:
                    if interleaving(s, t[i:], target[i:]):
                        return True

            return False


        return interleaving(s1, s2, s3)

# notes while solving:
# a a d b b c b c a c

# a a b c c
# d b b c a

# BT: find all possible interleavings and compare it with s3
# inefficient

# dp[i][j]
