[Problem](https://leetcode.com/problems/add-binary/)

## Bit Manipulation

During the interview, we may be asked to solve this problem without using the addition operator. In this case, we have to use bitwise operations to solve it.

The main idea is to use bitwise operations to compute `sum_without_carry` and `carry`. This can be done by using loop until the carry becomes zero, which is shown in [Editorial Approach 2](https://leetcode.com/problems/add-binary/editorial/?envType=study-plan-v2&envId=top-interview-150#approach-2-bit-manipulation).



- [Submission](https://leetcode.com/problems/add-binary/submissions/1783732582/) (Runtime: 0 ms, Memory: 17.70 MB)
- TC: $O(m + n)$, where $m$ and $n$ are the lengths of the two binary strings.
- SC: $O(max(m, n))$

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)

        while b:
            sum_without_carry = a ^ b
            carry = (a & b) << 1
            a, b = sum_without_carry, carry

        # return bin(a)[2:]
        return f"{(a):b}"

```


## Bit-by-Bit Computation (ripple-carry adder)

The solution below applies the two improvements mentioned in the `06_17_2025.py` code, which are using `divmod(...)` and `zfill(...)` functions. It is pretty straightforward.

cf.) The logic is identical to the Editorial's Approach 1.

- [Submission](https://leetcode.com/problems/add-binary/submissions/1783724822/) (Runtime: 3 ms, Memory: 17.8 MB)
- TC: $O(max(m, n))$, where $m$ and $n$ are the lengths of the two binary strings.
- SC: $O(max(m, n))$ (for `ans` array)



```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        ans = []
        for i in range(n - 1, -1, -1):
            total = carry
            total += int(a[i]) + int(b[i])

            carry, bit = divmod(total, 2)
            ans.append(str(bit))

        if carry == 1:
            ans.append("1")
        ans.reverse()

        return "".join(ans)

```

cf.) Here, we can also use `%` and `//` operators instead of `divmod` function to find the digit and carry.

- [Submission using `%` and `//` operators](https://leetcode.com/problems/add-binary/submissions/1783725000/) (Runtime: 3 ms, Memory: 18.11 MB)
