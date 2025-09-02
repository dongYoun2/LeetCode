# submission: https://leetcode.com/problems/candy/submissions/1756468676/
# runtime: 23 ms, memory: 20.2 MB

# 9 min
# TC: O(n), where n is the number of children (length of `ratings`)
# SC: O(n), for two additional arrays of size n (ans_f and ans_b)
# - space complexity can be reduced to O(1) by using only one answer array and updating it in place (https://leetcode.com/problems/candy/submissions/1571841520/)


# From LeetCode Top Interview 150 - Array / String

# this is a second time solving this problem. i first solved it on 03/12/2025 taking around an hour (but i was still proud that i solved the leetcode 'hard' problem on my own). the idea was really shocking at that time so as soon as i saw this problem for the second time today, i immediately noticed that i have to use two passes (forward and backward) to solve this problem. it's a really interesting problem.


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans_f = [1] * n
        ans_b = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                ans_f[i] = ans_f[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                ans_b[i] = ans_b[i+1] + 1

        return sum(max(a, b) for a, b in zip(ans_f, ans_b))


# notes while solving:
# forward pass (i-th child gets candies based on the left (i-1)-th child): 1 1 2
# backward pass: 2 1 1
# max between forward[i] and backward[i]: 2 1 2
