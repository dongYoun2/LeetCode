[Problem](https://leetcode.com/problems/zigzag-conversion/)

## Simulation Approach

This approach simulates the zigzag pattern by building each row one at a time. Below code is the improved version of the `09_08_2025.py` solution.

- [Submission](https://leetcode.com/problems/zigzag-conversion/submissions/1764196760/) (Runtime: 9 ms, Memory: 18.2 MB)
- TC: $O(n \cdot numRows)$, where $n$ is the length of the input string `s`.
- SC: $O(n)$, `rows`, the space used to store the result. although it's a nested list, the total number of characters stored is still `n`.

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Build each row left-to-right by walking down then up the rows
        rows = [[] for _ in range(numRows)]
        r, step = 0, 1  # step = +1 (down) or -1 (up)

        for ch in s:
            rows[r].append(ch)
            # Turn around at the first or last row
            if r == 0:
                step = 1
            elif r == numRows - 1:
                step = -1
            r += step

        return "".join("".join(r) for r in rows)

```


## Mathematical Approach (computing indices)

This approach computes the indices of characters in each row based on the periodicity of the zigzag pattern.

- [Submission](https://leetcode.com/problems/zigzag-conversion/submissions/1764194636/) (Runtime: 7 ms, Memory: 17.8 MB)
- TC: $O(n)$
- SC: $O(n)$

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s

        ans = []
        periodic = (numRows - 1) * 2

        for i in range(numRows):
            curr = i
            offset = i * 2

            while curr < n:
                ans.append(s[curr])
                offset = periodic - offset
                if offset == 0: # handle the first and last rows (skip duplicate indices)
                    offset = periodic - offset
                curr += offset

        return "".join(ans)

```


Maybe more readable code for the mathematical approach can be as follows. This first seperately addresses the firs/last rows and the middle rows in the first `for` loop. Then, for the middle rows, it uses two different offsets (`offset_down` and `offset_up`) and flag variable `toggle` to alternate between them.

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s

        period = 2 * (numRows - 1)
        ans = []

        for r in range(numRows):
            curr = r
            offset_down = period - 2 * r
            offset_up = 2 * r

            # First/last rows degenerate to a single fixed step = period
            if r == 0 or r == numRows - 1:
                while curr < n:
                    ans.append(s[curr])
                    curr += period
            else:
                # Middle rows alternate offset_down and offset_up
                toggle = True
                while curr < n:
                    ans.append(s[curr])
                    curr += offset_down if toggle else offset_up
                    toggle = not toggle

        return ''.join(ans)

```