[Problem](https://leetcode.com/problems/permutation-in-string/)


In complexity analysis, let $m$ and $n$ be the lengths of `s1` and `s2`, respectively.

## Sorting

One easy solution to consider is using sorting. We can maintain the sorted version of `s1` and compare it with the sorted version of each window of size $m$ in `s2`, which requires iterating over `s2` for $n - m + 1$ times. This approach can also been seen as one variant of the fixed-size sliding window approach.

[Submission](https://leetcode.com/problems/permutation-in-string/submissions/2012072884/)—Runtime: 3101 ms (beats 5.63%), Memory: 19.34 MB (beats 53.49%)

- TC: $O((n - m + 1) \cdot m \log m) \rightarrow O(n \cdot m \log m)$
- SC: $O(m)$ (since each sorted window uses extra space of size $m$)

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        target = sorted(s1)

        for i in range(n - m + 1):
            if sorted(s2[i:i+m]) == target:
                return True

        return False

```



## Variable-Size Sliding Window


Refer to the [05_08_2026.py](./05_08_2026.py) file for this approach.



## Fixed-Size Sliding Window


### Pre-initialized Window

[Submission](https://leetcode.com/problems/permutation-in-string/submissions/2012068127/)—Runtime: 47 ms (beats 29.50%), Memory: 19.48 MB (beats 19.21%)

- TC: $O(m + (n - m) \cdot 26) \rightarrow O(n)$ (build the first window in $O(m)$, then slide at most $n - m$ times with $O(26)$ counter comparisons per step)
- SC: $O(26) \rightarrow O(1)$

```python
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        need = Counter(s1)
        window = Counter(s2[:m])

        if window == need:
            return True

        for right in range(m, n):
            left = right - m

            window[s2[right]] += 1
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            if window == need:
                return True

        return False

```

### Incremental Window Build

[Submission](https://leetcode.com/problems/permutation-in-string/submissions/2012072156/)—Runtime: 26 ms (beats 42.27%), Memory: 19.57 MB (beats 19.21%)

- TC: $O(26 \cdot n) \rightarrow O(n)$ (each index is visited once; each step does $O(26)$ counter comparisons)
- SC: $O(26) \rightarrow O(1)$

```python
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        need = Counter(s1)
        window = Counter()

        for right in range(n):
            # expand window
            window[s2[right]] += 1

            # keep window size at most m
            if right >= m:
                left = right - m
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]

            # check only when window size is m
            if right >= m - 1 and window == need:
                return True

        return False

```



### No Full Window Comparison

[Submission](https://leetcode.com/problems/permutation-in-string/submissions/2012072320/)—Runtime: 52 ms (beats 23.76%), Memory: 19.21 MB (beats 94.60%)

- TC: $O(n + m) \rightarrow O(n)$ (build the first window in $O(m)$, then slide at most $n - m$ times with $O(1)$ match-count updates per step)
- SC: $O(26 + 26) \rightarrow O(1)$

```python
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        need = Counter(s1)
        window = Counter(s2[:m])

        # matches = number of chars whose counts are equal
        matches = 0
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if need[ch] == window[ch]:
                matches += 1

        for right in range(m, n):
            if matches == 26:
                return True

            left = right - m

            r_char = s2[right]
            l_char = s2[left]

            # add right char
            before = window[r_char] == need[r_char]
            window[r_char] += 1
            after = window[r_char] == need[r_char]

            if before and not after:
                matches -= 1
            elif not before and after:
                matches += 1

            # remove left char
            before = window[l_char] == need[l_char]
            window[l_char] -= 1
            after = window[l_char] == need[l_char]

            if before and not after:
                matches -= 1
            elif not before and after:
                matches += 1

        return matches == 26

```
<br>

- **Variable-size sliding window approach** and **fixed-size sliding window approach with no full window comparison** are technically optimal solutions since time complexity remains the same even when the number unique characters are not bounded by a constant; they are more general solutions.
- During the interview, I think the best strategy is to go with the **fixed size sliding window with pre-initialized window** solution since it is more intuitive and easier to implement as well as the code is more readable. Then, when the interview asks whether the solution can be optimized for the general case (when the strings can contain any characters) or whether counter comparison (`window == need`) can be optimized, we can enhance the solution to the **fixed-size sliding window with no full window comparsion** approach.
