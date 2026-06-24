# submission: https://leetcode.com/problems/random-pick-with-weight/submissions/2044582668/
# memory limit exceeded (check the failed case)
# 25 min

# symbols:
# - n: length of `w` array
# - g: gcd of all ingegers in `w`
# - m: size of the `candidates` array; equivalent to the "sum(w) / g"

# TC: 
# - constructor: O(n + m)
# - pickIndex: O(1)
# SC:
# - constructor: O(m)
# - pickIndex: O(1)

# worst case:
# g = 1, and m = sum(w) / 1 = 10^4 * 10^5 = 10^9 (since n and w[i] are at most 10^4 and 10^5 respectively)
# -> this is the reason why the code got memory limit exceeded error


# the solution below's logic is correct, but the memory usage is infeasible.

# i first simply considered constructing the array of size sum(w) where the elements are the indices of `w`, and each element is repeated `w[i]` times. then, once i shuffle the array only once, i can pick an index randomly following the weight probability distribution in O(1) time (`pickIndex` method). however, i noticed the array of size sum(w) is too large, so i thought of reducing it using the greatest common divisor, but this cannot solve the issue since there may be a case where the gcd is 1 so the size of the array is still sum(w) instead of sum(w) / g, which is actually the worst case scenario.

# cf.) after submitting the code, i spent additional 19 minutes to think of a better solution (so total 44 min spent on this problem), but couldn't solve it. once i saw the solution, i was flabbergasted by the idea, lol. for a correct and intended solution, refer to the README.md.


from functools import reduce
import math
import random


class Solution:

    def __init__(self, w: List[int]):
        gcd = reduce(math.gcd, w)
        reduced_w = [e // gcd for e in w]

        candidates = []
        for i, w in enumerate(reduced_w):
            candidates.extend([i] * w)
        
        random.shuffle(candidates)
        self.candidates = candidates


    def pickIndex(self) -> int:
        pos = random.randrange(len(self.candidates))
        return self.candidates[pos]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
