# 61 min
# wrong solution
# this only works when k < 3 (fails when k >= 3).


# chose from a neetcode "sliding window" category.

# i directly approached with the sliding window technique since i chose from the sliding window category. so i simulated the process, but failed to confirm the completeness of the algorithm when k >= 3. for example, when k = 3, n = 3, and maxPts = 10, the below solution only considers the below cases:

# 1. (3,) --> p: 0.1
# 2. (1, 2) --> p: 0.1 * 0.1 = 0.01
# 3. (1, 1, 1) --> p: 0.1 * 0.1 * 0.1 = 0.001

# therefore, it misses the case (2, 1), where the probability is 0.1 * 0.1 = 0.01. so the below algorithm returns 0.11100, whereas the expected answer is 0.12100.

# the correct approach is to first find the recurrent relation of the probability, which requires a O(n * maxPts) time DP (naive) solution. then, we can use sliding window technique to optimize this DP solution to O(n) time. refer to the README.md for details.

# cf.) `maxPts` is the same as the window size 
# cf.) i was shortsighted and could not think of other algorithms as i chose from the "sldiing window" category..


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        scores = [1.0] * (n+1)
        w_sz = maxPts
        ans = 0
        for left in range(1, n+1):
            for i in range(left, min(left+w_sz, n+1)):
                scores[i] *= 0.1
                if k <= i <= n:
                    ans += scores[i]

            if left == k:
                break

        return ans
