[Problem](https://leetcode.com/problems/add-binary/)

## Bit Manipulation

The main idea is to use bitwise operations to compute `sum_with_carry` and `sum_without_carry`. This can be done by the code below or by using loop until the carry becomes zero, which is shown in [Editorial Approach 2](https://leetcode.com/problems/add-binary/editorial/?envType=study-plan-v2&envId=top-interview-150#approach-2-bit-manipulation).



- [Submission](https://leetcode.com/problems/add-binary/submissions/) (Runtime: 4 ms, Memory: 17.69 MB)
- TC: $O(m + n)$, where $m$ and $n$ are the lengths of the two binary strings.
- SC: $O(1)$ (Output storage is not counted)
<br>

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)

        sum_with_carry = a ^ b
        sum_without_cary = (a & b) << 1

        # return bin(sum_with_carry + sum_without_cary)[2:]
        return f"{(sum_with_carry + sum_without_cary):b}"

```