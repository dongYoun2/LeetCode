[Problem](https://leetcode.com/problems/bitwise-and-of-numbers-range/)


## Bitwise Operations

The key idea of this problem is to find the common prefix of two binary numbers. We can right shift the bits of both numbers until they become equal, then we can left shift back with the same number of right shifts to get the final result.


[Submission](https://leetcode.com/problems/bitwise-and-of-numbers-range/submissions/2093170318/)—Runtime: 5 ms (beats 46.97%), Memory: 19.23 MB (beats 51.09%)

- TC: $O(32) \rightarrow O(1)$ (at most one iteration per bit)
- SC: $O(1)$

```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0

        # Remove differing bits until left and right become equal.
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1

        # Restore the common prefix.
        return left << shift

```