[Problem](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/)



## Sliding Window (Optimal)

The key trick is to simulate the rotations by **doubling the string**. Then, we can use a sliding window technique to find the minimum number of flips. I was flabbergasted by this; I remember I saw this trick in another problem (cannot found which one it is though) in the past, but forgot about it.


cf.) When the problem has array rotation or circular shift as a dependency, common patterns I found so far are:
1. Greedy approach: if I need to try every starting point, but can eliminate some. ([134. Gas Station](../134.%20Gas%20Station/README.md))
2. Sliding window (+ doubling the array): if I am dealing with subarrays or windows that needs to be wrapped around. (this problem)


[Submission](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/submissions/1981950748/)—Runtime: 355 ms (beats 51.36%), Memory: 19.88 MB (beats 81.47%)


- TC: $O(n)$
- SC: $O(1)$

```python
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ss = s + s  # simulate rotations

        # mismatches for two patterns
        # first pattern (starts with 0): 010101010...
        # second pattern (starts with 1): 101010101...
        diff1 = diff2 = 0
        ans = n

        for right in range(len(ss)):
            # expected chars
            p1 = '0' if right % 2 == 0 else '1'
            p2 = '1' if right % 2 == 0 else '0'

            # add right
            if ss[right] != p1:
                diff1 += 1
            if ss[right] != p2:
                diff2 += 1

            # remove left (keep window size n)
            if right >= n:
                left = right - n
                lp1 = '0' if left % 2 == 0 else '1'
                lp2 = '1' if left % 2 == 0 else '0'

                if ss[left] != lp1:
                    diff1 -= 1
                if ss[left] != lp2:
                    diff2 -= 1

            # valid window
            if right >= n - 1:
                ans = min(ans, diff1, diff2)

        return ans

```