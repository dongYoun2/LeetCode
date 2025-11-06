[Problem](https://leetcode.com/problems/single-number-ii/)


## Bit Manipulation (Similar to the Editorial Approach 5)

The key idea for this solution is to to keep track of the bits that appear once and twice so far. We can easily find the bit that appeared three times simply by checking if the bit is set to both `seen_once` and `seen_twice`. Then, we can clear this bit from both, which eventually bits that appeared only once will be left in the `seen_once`.

To do this, we need to use bitwise operations to update `seen_once` and `seen_twice` with the fired bits of `num`. Note that we are using XOR in `seen_once ^= num` so that bits that haven't appeared yet will be set and bits that already appeared once will be cleared (since they need to be moved to `seen_twice`, where it's done in the line `seen_twice |= (seen_once & num)`).

cf.) I was really amazed by this solution—so elegant and concise.


- [Submission](https://leetcode.com/problems/single-number-ii/submissions/1822814303/) (Runtime: 3 ms, Memory: 19.30 MB)
- TC: $O(n)$, where $n$ is the number of elements in `nums`.
- SC: $O(1)$

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # bits appearing once and twice so far, respectively (mod 3 == 1, mod 3 == 2)
        seen_once = seen_twice = 0

        for num in nums:
            seen_twice |= (seen_once & num)
            seen_once ^= num

            # compute mask of bits that just reached count == 3
            # (i.e., bits in both seen_once & seen_twice):
            common_mask = ~(seen_once & seen_twice)
            # clear bits that have appeared three times from both seen_once and seen_twice:
            seen_once &= common_mask
            seen_twice &= common_mask

        return seen_once

```