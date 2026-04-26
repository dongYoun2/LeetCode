[Problem](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/)


## Sliding Window (Optimal)

- TC: $O(n)$ (True linear time; doesn't change when `s` can contain any characters)
- SC: $O(k) \rightarrow O(m) \rightarrow O(1)$, where $m$ is the number of unique characters in a window of size $k$ ($m \leq \min(26, k)$; 26 is the number of lowercase English letters)


### Using Fixed Window Size 

This solution is optimized from the `04_26_2026.py` solution. Simply changed `all(v == 1 for v in cntr.values())` -> `len(cntr) == k`. This avoids iterating over the counter values for each window. Since the window size is fixed to $k$, for all characters in the window to be non-repeated, the number of unique characters in the window must be $k$. therefore, checking whether the length of the counter is equivalent to $k$ is sufficient.

[Submission](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/submissions/1988864890/)—Runtime: 17 ms (beats 12.08%), Memory: 19.50 MB (beats 12.92%)

```python
from collections import Counter

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        if k > n:
            return 0

        cntr = Counter(s[:k])
        ans = int(len(cntr) == k)
        for i in range(k, n):
            c_left = s[i-k]
            cntr[c_left] -= 1

            if cntr[c_left] == 0:
                del cntr[c_left]
            
            c_right = s[i]
            cntr[c_right] += 1

            ans += len(cntr) == k

        return ans

```



### Using Variable Window Size

The key idea is to expand the window by one character at a time, and shrink the window until the window contains no repeated characters. therefore the window size is variable. to find the proper substring, we need to check if the window size is equal to $k$ after each expansion and shrinkage.

Variable window technique is more general (used in many problems), but it's slightly more complex than the fixed window technique.


[Submission](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/submissions/1988870616/)—Runtime: 24 ms (beats 5.83%), Memory: 19.23 MB (beats 85.42%)


```python
from collections import Counter

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        count = Counter()   # char -> frequency in current window
        left = ans = 0

        for right in range(n):
            # Step 1: expand window (add s[right])
            count[s[right]] += 1

            # Step 2: shrink until no duplicates of s[right]
            while count[s[right]] > 1:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            # Step 3: if window size == k -> valid substring
            if right - left + 1 == k:
                ans += 1

                # shrink to look for next window
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

        return ans

```