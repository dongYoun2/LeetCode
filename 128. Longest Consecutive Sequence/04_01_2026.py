# submission: https://leetcode.com/problems/longest-consecutive-sequence/submissions/1965902695/
# runtime: 108 ms (beats 8.81%), memory: 37.33 MB (beats 13.48%)
# 28 min

# TC: O(n)
# SC: O(n) (converting to set + two dictionaries)


# i used two dictionaries, l2u where the lower bound maps to the upper bound of an interval, and u2l where the upper bound maps to the lower bound. for each (unique) number, i check if there exists an interval starting at n+1, and an interval ending at n-1. then, i merge them into one bigger interval. the final answer would be the maximum difference between the lower and upper bound of the all intervals. so this is basically an inteval-merging with hash maps solution.

# it's not a standard solution, but this is the solution i came up with from scratch. a more standard and intuitive solution is "start of sequence + set" solution (see the README.md's Hash Map Solution).

# i learned that we can use `pop(key, None)` to delete a key from a dictionary without raising a KeyError.

# cf.) there's also a union-find solution for this problem. refer to the README.md for details.


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        l2u = {}
        u2l = {}

        for n in nums:
            l, u = n+1, n-1

            new_u = l2u.get(l, n)
            new_l = u2l.get(u, n)

            l2u.pop(l, None)
            l2u.pop(n, None)

            u2l.pop(u, None)
            u2l.pop(n, None)

            l2u[new_l] = new_u
            u2l[new_u] = new_l
        
        ans = 0
        for k, v in l2u.items():
            ans = max(ans, v - k + 1)
        
        return ans
