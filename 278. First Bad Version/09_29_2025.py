# submission: https://leetcode.com/problems/first-bad-version/submissions/1786766673/
# runtime: 40 ms, memory: 17.5 MB

# 7 min
# TC: O(log n), where n is the input number n
# SC: O(1)


# This is a simple binary search problem. The key is to find the first bad version with a minimum number of calls to the isBadVersion API.

# however, in the code below, we call the isBadVersion API twice for each iteration of the binary search. this can be optimized by calling only once. the code can be found here: https://leetcode.com/problems/first-bad-version/submissions/1440951028/



# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2

            if isBadVersion(m):
                if not isBadVersion(m - 1):
                    return m
                else:
                    r = m - 1
            else:
                l = m + 1
