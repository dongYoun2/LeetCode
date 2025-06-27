[Problem](https://leetcode.com/problems/reverse-bits/)

## Byte by Byte with Memoization

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