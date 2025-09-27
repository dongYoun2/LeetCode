# submission: https://leetcode.com/problems/counting-bits/submissions/1783751132/
# runtime: 3 ms, memory: 18.61 MB
# this solution solves the follow-up question.

# 11 min
# TC: O(n), where n is the input integer.
# SC: O(1), not counting the output array.

# coming up with the O(n log n) time solution is pretty straightforward. to solve it in O(n) time with single pass, we can apply dynamic programming. the recurrent relation is ans[i] = ans[i // 2] + i % 2. since there are division and modulo operations by 2, we can utilize bit manipulation as well (ans[i] = ans[i >> 1] + i & 1).


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            q, r = divmod(i, 2) # r indicates the trailing bit
            ans[i] = ans[q] + r

        return ans
