[Problem](https://leetcode.com/problems/remove-duplicate-letters/description/)


## Greedy with Stack Approach

This solution is written by ChatGPT.

- [Submission](https://leetcode.com/problems/remove-duplicate-letters/submissions/1800443203/) (Runtime: 3 ms, Memory: 17.79 MB)
- TC: $O(n)$, where $n$ is the length of the input string `s`.
- SC: $O(k)$ -> $O(1)$, where $k$ is the number of unique characters in the input string `s`. It's asymptotically $O(1)$ since the maximum value of $k$ is 26 (the number of letters in the English alphabet).

```python
from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Count remaining occurrences of each character
        cntr = Counter(s)
        stack = []
        seen = set()    # Tracks characters already in stack

        for ch in s:
            cntr[ch] -= 1

            if ch in seen:
                continue

            # Remove larger chars that appear later (to keep result lexicographically small)
            while stack and ch < stack[-1] and cntr[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)

```

I spent around 50 minutes to solve this problem, but I couldn't though I knew that I had to use the stack data structure. In addition to using stack, the problem requires to solve it in a greedy manner. For me, I always feel like greedy problems are tough to come up with a solution. I guess I need some more practice.

cf.) Instead of using the `Counter`, we can build a **last occurence index map** for each character, and use it to determine if a character can be removed from the stack (Editorial's Approach 2). The time and space complexity are the same as the above solution. One intersting thing is that last occurence map can be created with `last_occurrence = {c: i for i, c in enumerate(s)}`. In dictionary comprehension, duplicate characters (keys) will be simply replaced by the last occurrence. For more details, refer to the Editorial's Approach 2.