[Problem](https://leetcode.com/problems/powx-n/)


# Binary Exponentiation

This algorithm is regarded as a divide-and-conquer algorithm.

- TC: $O(\log |n|)$, where $n$ is the input exponent `n`.
- SC: $O(1)$ for the iterative approach, $O(\log |n|)$ for the recursive approach.


## Iterative Approach

Unlike [07_19_2025.py](07_19_2025.py) and [07_02_2026.py](07_02_2026.py)'s iterative solutions, this standard solution reuses the squaring results instead of recomputing them, and thus, the time complexity is more optimal.


[Submission](https://leetcode.com/problems/powx-n/submissions/2053600705/)—Runtime: 2 ms (beats 20.84%), Memory: 19.54 MB (beats 18.76%)

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1.0

        while n > 0:
            if n % 2 == 1:
                ans *= x

            x *= x
            n //= 2

        return ans

```

cf.) Though this standard iterative code's runtime is slower than [07_19_2025.py](07_19_2025.py) and [07_02_2026.py](07_02_2026.py) in practice, the complexity analysis is more optimal (Probably this 2 ms difference is noise).

<br>


## Recursive Approach


[Submission](https://leetcode.com/problems/powx-n/submissions/2053602112/)—Runtime: 0 ms (beats 100.00%), Memory: 19.40 MB (beats 85.81%)

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1.0

            half = power(x, n // 2)

            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            return 1 / power(x, -n)

        return power(x, n)

```

cf.) Other recursive implementation can be found in the [07_19_2025_recursive.py](07_19_2025_recursive.py).