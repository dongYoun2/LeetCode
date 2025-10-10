[Problem](https://leetcode.com/problems/minimum-window-substring/)

## Sliding Window

The code below is written by ChatGPT. Note that it uses the advtanges of the `Counter` class. `Counter` allows us to gracefully handle the membership check and the count update in a single operation. Because of this, `need` contains not only the characters of `t`, but also the characters of `s` that are not in `t`.

cf.) This [submission](https://leetcode.com/problems/minimum-window-substring/submissions/1796712072/) (Runtime: 50 ms, Memory: 18.21 MB) uses a normal dictionary instead of the `Counter`. Time and space complexities are same. For details, refer to the **Notes** part of the submission.

- [Submission](https://leetcode.com/problems/minimum-window-substring/submissions/1796670994/) (Runtime: 63 ms, Memory: 18.27 MB)
- TC: $O(m + n)$, where $m$ and $n$ are the lengths of `s` and `t`, respectively.
- SC: $O(1)$, since the input strings only contain upper and lower case English letters.


```python
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        assert s and t
        if len(t) > len(s): return ''

        need = Counter(t)                 # counts of required chars
        missing = len(t)                  # total chars still needed
        ans_left = ans_right = 0
        left = 0

        # expand window with right pointer
        for right, ch in enumerate(s, 1):  # right is 1-based to slice easily
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            # when valid, shrink from the left
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if ans_right == 0 or right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right

                # move left forward to look for next best window
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[ans_left:ans_right]

```