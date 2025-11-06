[Problem](https://leetcode.com/problems/reverse-bits/)


## Bit by Bit Computation

Refer to the [06_26_2025.py](06_26_2025.py) solution.


## Byte by Byte with Memoization (Follow-up Question)

This solves the follow-up question: "If this function is called many times, how would you optimize it?"

This solution processes the input integer byte by byte, reversing each byte using a memoized function. The final result is constructed by shifting the reversed bytes into their correct positions. Reversing a byte is done using a mathematical trick that utilizes bitwise operations explained [here](https://arc.net/l/quote/cazdsxbs).

cf.) `0xFF` is `11111111` in binary, which is used to mask the last 8 bits of the integer.

- [Submission](https://leetcode.com/problems/reverse-bits/submissions/1460183019/) (runtime: 42 ms, memory: 18 MB)
- TC: $O(1)$, although the loop exists,  it runs a fixed number of times (4 iterations for 32 bits).
- SC: $O(1)$
<br>

```python
import functools


class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 24
        while n:
            ret += self.reverseByte(n & 0xFF) << power
            n = n >> 8
            power -= 8
        return ret

    # memoization with decorator
    @functools.lru_cache(maxsize=256)
    def reverseByte(self, byte):
        return (byte * 0x0202020202 & 0x010884422010) % 1023
```

During the interview, of course we don't have to know the details of the above math trick. We can simply state that the idea (to solve the follow-up question) is to precompute or cache the reversed byte (8-bits) values and use them to construct the final result. In this case, the `reverseByte(...)` function will simply be as follows:

```python
@functools.lru_cache(maxsize=256)
    def reverseByte(self, byte: int) -> int:
        """Reverse the 8 bits of `byte` (0..255)."""
        r = 0
        for _ in range(8):
            r = (r << 1) | (byte & 1)
            byte >>= 1
        return r

```